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
            discount = Discount(percentage=Decimal(0))
            span.set_attribute("given_discount_percentage", str(discount.percentage))
            return discount

    def place_order(self, code, identity, amount, date, status="validating"):
        """Place a new order.

        For a configured list of identity the status will be "approved".
        """
        with self.tracer.start_as_current_span("OrderUseCase.place_order", kind=SERVER):

            if identity in settings.APPROVED_ORDER_IDENTITIES:
                status = "approved"

            return self.store.create(code, identity, amount, status, date)

    def calculate_cashback(self, amount_cents):
        percentage = 10

        if 100000 < amount_cents <= 150000:
            percentage = 15

        if 150000 < amount_cents:
            percentage = 20

        amount = (percentage * amount_cents) / 100.0
        return (int(amount), percentage)

    def list_approved_orders(self):
        """List approved orders."""
        with self.tracer.start_as_current_span(
            "OrderUseCase.list_approved_orders", kind=SERVER
        ):
            return self.store.query_status("approved")

    def list_orders_with_cashback(self):
        """List orders with cashback."""
        with self.tracer.start_as_current_span(
            "OrderUseCase.list_orders_with_cashback", kind=SERVER
        ):
            orders = []
            entities = self.store.query_all()
            for entity in entities:
                amount, percentage = self.calculate_cashback(entity.amount_cents)
                entity.amount_cashback_cents = amount
                entity.cashback_percentage = percentage
                orders.append(entity)
            return orders
