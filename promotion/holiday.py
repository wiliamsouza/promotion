"Holiday use case implementation."
import datetime
import uuid
from decimal import Decimal

from opentelemetry import trace

from promotion import settings
from promotion.entity import Discount
from promotion.protocol import DiscountDataStore

SERVER = trace.SpanKind.SERVER


class HolidayUseCase:
    """Implements DiscountUseCase interface."""

    def __init__(self, store: DiscountDataStore, tracer) -> None:
        self.store = store
        self.tracer = tracer

    def discount(self, user_id: uuid.UUID) -> Discount:
        """Give discount if today is black friday."""
        with self.tracer.start_as_current_span(
            "HolidayUseCase.create", kind=SERVER
        ) as span:

            span.set_attribute("is_black_friday?", False)
            discount = Discount(percentage=Decimal(0))
            if self.store.query(user_id) == datetime.date.today():
                span.set_attribute("is_black_friday?", True)
                discount.percentage = settings.BLACK_FRIDAY_PERCENTAGE

            span.set_attribute("given_discount_percentage", str(discount.percentage))
            return discount
