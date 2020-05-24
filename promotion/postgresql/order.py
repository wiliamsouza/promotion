"""Order data store implementation."""
import datetime
import decimal
import uuid
from typing import Optional

from opentelemetry import trace
from opentelemetry.trace import status as trace_status
from sqlalchemy.exc import SQLAlchemyError

from promotion.entity import User as UserEntity
from promotion.entity import Order as OrderEntity
from promotion.postgresql import User as UserModel
from promotion.postgresql import Order as OrderModel

SERVER = trace.SpanKind.SERVER


class OrderDataStore:
    """Implements order data store interface."""

    def __init__(self, database, tracer) -> None:
        self.database = database
        self.tracer = tracer

    def query(self, order_code: uuid.UUID) -> Optional[OrderEntity]:
        """Query filtering order for the given code."""

        with self.tracer.start_as_current_span(
            "OrderDataStore.query", kind=SERVER
        ) as span:

            span.set_attribute("is_order_found?", False)
            span.set_attribute("order_code", str(order_code))
            order = (
                self.database.query(OrderModel).filter(OrderModel.code == order_code).first()
            )
            if order:
                span.set_attribute("is_order_found?", True)
                return OrderEntity(
                    amount_cents=order.amount_cents,
                    code=order.code,
                    status=order.status,
                    identity=order.identity,
                    date=order.date,
                )

        return None

    def create(self, code: uuid.UUID, identity:str , amount_cents: decimal.Decimal, status: str, date: datetime.date) -> OrderEntity:
        """Store an order in database."""
        with self.tracer.start_as_current_span(
            "OrderDataStore.create", kind=SERVER
        ) as span:

            order = OrderModel(
                code=code,
                amount_cents=amount_cents,
                status=status,
                identity=identity,
                date=date,
            )
            self.database.add(order)
            try:
                self.database.commit()
            except SQLAlchemyError:
                self.database.rollback()

            span.set_status(
                trace_status.Status(
                    canonical_code=trace_status.StatusCanonicalCode.OK,
                    description="Success creating order",
                )
            )
            return OrderEntity(
                amount_cents=order.amount_cents,
                code=order.code,
                status=order.status,
                identity=order.identity,
                date=order.date,
            )
