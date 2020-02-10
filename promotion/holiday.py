"Holiday use case implementation."
import datetime

from promotion import settings


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
            discount["percentage"] = settings.BLACK_FRIDAY_PERCENTAGE

        return discount
