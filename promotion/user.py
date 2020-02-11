"User use case implementation."
import datetime

from promotion import settings


class UserUseCase:
    """Implements user use case interface."""

    def __init__(self, store):
        self.store = store

    def discounts(self, user_id):
        """Retrieve all users discounts available."""
        return self.birthday(user_id)

    def birthday(self, user_id):
        """Give discount if is the exact date a person was born."""
        discount = {"percentage": 0}
        user = self.store.user(user_id)
        if user and user.birthday == datetime.date.today():
            discount["percentage"] = settings.USER_BIRTHDAY_PERCENTAGE

        return discount

    def create(self, user_id, birthday):
        """Create an user."""
        return self.store.create(user_id, birthday)
