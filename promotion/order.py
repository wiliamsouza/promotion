"Order use case implementation."
import datetime
import logging
import uuid
from decimal import Decimal

from opentelemetry import trace

from promotion.entity import Discount
from promotion.protocol import DiscountDataStore

SERVER = trace.SpanKind.SERVER

logger = logging.getLogger(__name__)


class OrderUseCase:
    """Implements DiscountUseCase interface."""

    def __init__(self, store: DiscountDataStore, tracer) -> None:
        self.store = store
        self.tracer = tracer

    def discount(self, user_id: uuid.UUID) -> Discount:
        """Give discount if the order amount is in the defined range."""
        with self.tracer.start_as_current_span(
            "OrderUseCase.discount", kind=SERVER
        ) as span:
            discount = Discount(percentage=Decimal(0))
            return discount

    def create(self, code, identity, amount, status, date):
        """Create an order."""
        with self.tracer.start_as_current_span("OrderUseCase.create", kind=SERVER):
            return self.store.create(code, identity, amount, status, date)
