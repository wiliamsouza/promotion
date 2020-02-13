"""User data store implementation."""
import datetime
from typing import Dict
import uuid

from promotion.postgresql import User
from promotion.entity import User as UserEntity


class UserDataStore:
    """Implements user data store interface."""

    def __init__(self, database) -> None:
        self.database = database

    def query(self, user_id: uuid.UUID) -> UserEntity:
        "Query filtering user for the given ID."
        user = self.database.query(User).filter(User.id == user_id).first()
        return UserEntity(birthday=user.birthday)

    def create(self, user_id: uuid.UUID, birthday: datetime.date):
        """Store an user in database."""
        user = User(id=user_id, birthday=birthday)
        self.database.add(user)
        self.database.commit()

        # TODO: Change to return entity.User
        return user
