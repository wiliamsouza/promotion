"""User data store implementation."""
import uuid


class HolidayDataStore:
    """Implements holiday data store interface."""

    def __init__(self, date):
        self.date = date

    # pylint: disable=unused-argument
    def query(self, user_id: uuid.UUID):
        "Query black friday date."
        return self.date
