"""User data store implementation."""
import datetime


class HolidayDataStore:
    """Implements holiday data store interface."""

    def __init__(self, date):
        self.date = date

    def query(self, *args, **kwargs):
        return self.date
