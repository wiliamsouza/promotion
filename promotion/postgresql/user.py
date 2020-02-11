"""User data store implementation."""
from promotion.postgresql import User


class UserDataStore:
    """Implements user data store interface."""

    def __init__(self, database):
        self.database = database

    def query(self, user_id):
        # TODO: Change to return entity.User
        return self.user(user_id)

    def user(self, user_id):
        "Query filtering user for the given ID."
        return self.database.query(User).filter(User.id == user_id).first()

    def create(self, user_id, birthday):
        """Store an user in database."""
        user = User(id=user_id, birthday=birthday)
        self.database.add(user)
        self.database.commit()

        # TODO: Change to return entity.User
        return user
