"User use case implementation."
import datetime


class UserUseCase:
    """Implements user use case interface."""

    def __init__(self, store):
        self.store = store

    def discounts(self, *args, **kwargs):
        """Retrieve all users discounts available."""
        # TODO: Validate args and kargs
        # TODO: Add logs
        return self.birthday(kwargs["user_id"])

    def birthday(self, user_id):
        """Give discount if is the exact date a person was born."""
        discount = {"percentage": 0}
        user = self.store.user(user_id)
        if user and user.birthday == datetime.date.today():
            # TODO: Change to get from environment variable
            discount["percentage"] = 5

        return discount
