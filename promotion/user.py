"User use case implementation."
import datetime
import logging
import uuid
from decimal import Decimal

from argon2 import PasswordHasher

from opentelemetry import trace

from promotion import settings
from promotion.entity import Discount
from promotion.protocol import DiscountDataStore

SERVER = trace.SpanKind.SERVER

logger = logging.getLogger(__name__)


class UserUseCase:
    """Implements DiscountUseCase interface."""

    def __init__(self, store: DiscountDataStore, tracer) -> None:
        self.store = store
        self.tracer = tracer

    def discount(self, user_id: uuid.UUID) -> Discount:
        """Give discount if is the exact date a person was born."""
        with self.tracer.start_as_current_span(
            "UserUseCase.discount", kind=SERVER
        ) as span:

            discount = Discount(percentage=Decimal(0))

            user = None
            try:
                uuid.UUID(str(user_id))
                user = self.store.query(user_id)
            except ValueError:
                logger.debug("Not valid user ID, not querying database.")

            span.set_attribute("is_user_birthday?", False)
            if user:
                span.set_attribute("user birthday", str(user.birthday))
                today = datetime.date.today()
                span.set_attribute("today", str(today))
                if (
                    user.birthday.day == today.day
                    and user.birthday.month == today.month
                ):
                    span.set_attribute("is_user_birthday?", True)
                    discount.percentage = settings.USER_BIRTHDAY_PERCENTAGE

            span.set_attribute("given_discount_percentage", str(discount.percentage))
            return discount

    def create(self, user_id, birthday, identity, email, name, password):
        """Create an user."""
        with self.tracer.start_as_current_span("UserUseCase.create", kind=SERVER):
            ph = PasswordHasher()
            password_hash = ph.hash(password)
            return self.store.create(user_id, birthday, identity, email, name, password_hash)

    def retrieve_user_by_email(self, email):
        """List user by the given email."""
        with self.tracer.start_as_current_span("UserUseCase.list_user_by_email", kind=SERVER):
            return self.store.query_by_email(email)
