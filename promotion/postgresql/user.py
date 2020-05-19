"""User data store implementation."""
import datetime
import uuid
from typing import Optional

from opentelemetry import trace
from opentelemetry.trace import status
from sqlalchemy.exc import SQLAlchemyError

from promotion.entity import User as UserEntity
from promotion.postgresql import User as UserModel

SERVER = trace.SpanKind.SERVER


class UserDataStore:
    """Implements user data store interface."""

    def __init__(self, database, tracer) -> None:
        self.database = database
        self.tracer = tracer

    def query(self, user_id: uuid.UUID) -> Optional[UserEntity]:
        """Query filtering user for the given ID."""

        with self.tracer.start_as_current_span(
            "UserDataStore.query", kind=SERVER
        ) as span:

            span.set_attribute("is_user_found?", False)
            span.set_attribute("user_id", str(user_id))
            user = (
                self.database.query(UserModel).filter(UserModel.id == user_id).first()
            )
            if user:
                span.set_attribute("is_user_found?", True)
                return UserEntity(
                    birthday=user.birthday,
                    identity=user.identity,
                    email=user.email,
                    name=user.name,
                    password=user.password,
                )

        return None

    def create(self, user_id: uuid.UUID, birthday: datetime.date, identity: str, email: str, name: str, password: str) -> UserEntity:
        """Store an user in database."""
        with self.tracer.start_as_current_span(
            "UserDataStore.create", kind=SERVER
        ) as span:

            user = UserModel(
                id=user_id,
                birthday=birthday,
                identity=identity,
                email=email,
                name=name,
                password=password,
            )
            self.database.add(user)
            try:
                self.database.commit()
            except SQLAlchemyError:
                self.database.rollback()

            span.set_status(
                status.Status(
                    canonical_code=status.StatusCanonicalCode.OK,
                    description="Success creating user",
                )
            )
            return UserEntity(
                birthday=user.birthday,
                identity=user.identity,
                email=user.email,
                name=user.name,
                password=user.password,
            )
