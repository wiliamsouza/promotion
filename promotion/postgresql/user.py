"""User data store implementation."""
from typing import Optional

import datetime
import uuid

from promotion.entity import User as UserEntity
from promotion.postgresql import User as UserModel


class UserDataStore:
    """Implements user data store interface."""

    def __init__(self, database) -> None:
        self.database = database

    def query(self, user_id: uuid.UUID) -> Optional[UserEntity]:
        """Query filtering user for the given ID."""
        user = self.database.query(UserModel).filter(UserModel.id == user_id).first()
        if user:
            return UserEntity(birthday=user.birthday)

        return None

    def create(self, user_id: uuid.UUID, birthday: datetime.date) -> UserEntity:
        """Store an user in database."""
        user = UserModel(id=user_id, birthday=birthday)
        self.database.add(user)
        self.database.commit()

        return UserEntity(user_id=user.id, birthday=user.birthday)
