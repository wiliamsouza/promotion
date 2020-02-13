"Holiday use case implementation."
import datetime
from typing import Dict
import uuid
from decimal import Decimal

from promotion import settings
from promotion.protocol import DiscountDataStore
from promotion.entity import Discount


class HolidayUseCase:
    """Implements DiscountUseCase interface."""

    def __init__(self, store: DiscountDataStore) -> None:
        self.store = store

    def discount(self, user_id: uuid.UUID) -> Discount:
        """Give discount if today is black friday."""
        discount = Discount(percentage=Decimal(0))
        if self.store.query(user_id) == datetime.date.today():
            discount.percentage = settings.BLACK_FRIDAY_PERCENTAGE

        return discount
