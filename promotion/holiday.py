"Holiday use case implementation."
import datetime


class HolidayUseCase:
    """Implements holiday use case interface."""

    def __init__(self, store):
        self.store = store

    def discounts(self, *args, **kwargs):
        """Retrieve all holidays discounts available."""
        return self.black_friday()

    def black_friday(self):
        """Give discount if today is black friday."""
        discount = {"percentage": 0}
        if self.store.query() == datetime.date.today():
            # TODO: Change to get from environment variable
            discount["percentage"] = 10

        return discount
