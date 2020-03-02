"User use case implementation."
import datetime
import logging
import uuid
from decimal import Decimal

from promotion import settings
from promotion.entity import Discount
from promotion.protocol import DiscountDataStore


class UserUseCase:
    """Implements DiscountUseCase interface."""

    def __init__(self, store: DiscountDataStore) -> None:
        self.store = store

    def discount(self, user_id: uuid.UUID) -> Discount:
        """Give discount if is the exact date a person was born."""
        discount = Discount(percentage=Decimal(0))

        user = None
        try:
            uuid.UUID(str(user_id))
            user = self.store.query(user_id)
        except ValueError:
            logging.info("Not valid user ID, not querying database.")

        if user:
            today = datetime.date.today()
            if user.birthday.day == today.day and user.birthday.month == today.month:
                discount.percentage = settings.USER_BIRTHDAY_PERCENTAGE

        return discount

    def create(self, user_id, birthday):
        """Create an user."""
        return self.store.create(user_id, birthday)
