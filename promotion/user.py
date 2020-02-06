"User use case implementation."
import datetime


class UserUseCase:
    """Implements user use case interface."""

    def __init__(self, store):
        self.store = store

    def birthday(self, user_id):
        """Birthday discount percentage."""
        discount = {"percentage": 0}
        user = self.store.user(user_id)
        if user and user.birthday == datetime.date.today():
            # TODO: Change to get from environment variable
            discount["percentage"] = 5

        return discount
