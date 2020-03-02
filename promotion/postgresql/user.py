"""User data store implementation."""
import datetime
import uuid

from promotion.entity import User as UserEntity
from promotion.postgresql import User


class UserDataStore:
    """Implements user data store interface."""

    def __init__(self, database) -> None:
        self.database = database

    def query(self, user_id: uuid.UUID) -> UserEntity:
        "Query filtering user for the given ID."
        user = self.database.query(User).filter(User.id == user_id).first()
        if user:
            return UserEntity(birthday=user.birthday)

    def create(self, user_id: uuid.UUID, birthday: datetime.date) -> UserEntity:
        """Store an user in database."""
        user = User(id=user_id, birthday=birthday)
        self.database.add(user)
        self.database.commit()

        return UserEntity(user_id=user.id, birthday=user.birthday)
