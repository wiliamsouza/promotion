"Holiday use case implementation."
import datetime


class HolidayUseCase:
    """Implements holiday use case interface."""

    def __init__(self, date):
        self.date = date

    def black_friday(self):
        """Black friday discount percentage."""
        discount = {"percentage": 0}
        if self.date == datetime.date.today():
            # TODO: Change to get from environment variable
            discount["percentage"] = 10

        return discount
