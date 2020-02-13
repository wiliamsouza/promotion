"User use case implementation."
import datetime
from decimal import Decimal
from typing import Dict
import uuid

from promotion import settings
from promotion.protocol import DiscountDataStore
from promotion.entity import Discount


class UserUseCase:
    """Implements DiscountUseCase interface."""

    def __init__(self, store: DiscountDataStore) -> None:
        self.store = store

    def discount(self, user_id: uuid.UUID) -> Discount:
        """Give discount if is the exact date a person was born."""
        discount = Discount(percentage=Decimal(0))
        user = self.store.query(user_id)
        if user and user.birthday == datetime.date.today():
            discount.percentage = settings.USER_BIRTHDAY_PERCENTAGE

        return discount

    def create(self, user_id, birthday):
        """Create an user."""
        return self.store.create(user_id, birthday)
