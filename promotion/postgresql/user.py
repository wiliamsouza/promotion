"""User data store implementation."""
from promotion.postgresql import User


class UserDataStore:
    """Implements user data store interface."""

    def __init__(self, database):
        self.database = database

    def user(self, user_id):
        "Query filtering user for the given ID."
        return self.database.query(User).filter(User.id == user_id).first()
