"Order use case implementation."
import datetime
import logging
import uuid
from decimal import Decimal

from opentelemetry import trace

from promotion import settings
from promotion.entity import Discount
from promotion.protocol import DiscountDataStore

SERVER = trace.SpanKind.SERVER

logger = logging.getLogger(__name__)


class OrderUseCase:
    """Implements DiscountUseCase interface."""

    def __init__(self, store: DiscountDataStore, tracer) -> None:
        self.store = store
        self.tracer = tracer

    def discount(self, _user_id: uuid.UUID) -> Discount:
        """Give zero discount this implementation do not follow the same discount rules."""
        with self.tracer.start_as_current_span(
            "OrderUseCase.discount", kind=SERVER
        ) as span:
            span.set_attribute("given_discount_percentage", str(discount.percentage))
            discount = Discount(percentage=Decimal(0))
            return discount

    def place_order(self, code, identity, amount, date, status="validating"):
        """Place a new order.

        For a configured list of identity the status will be "approved".
        """
        with self.tracer.start_as_current_span("OrderUseCase.create", kind=SERVER):

            if identity in settings.APPROVED_ORDER_IDENTITIES:
                status = "approved"

            return self.store.create(code, identity, amount, status, date)
