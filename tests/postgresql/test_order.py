"""Tests for postgresql order data store implementation."""
import datetime
import decimal

from promotion.postgresql.order import OrderDataStore
from promotion.postgresql import Order

from ..factories import OrderFactory


def test_order_data_store(database, tracer):
    order = OrderFactory.create()
    assert database.query(Order).one()
    store = OrderDataStore(database, tracer)

    result = store.query(order.code)

    assert result.date == datetime.date.today()
    assert result.amount == decimal.Decimal('99.90')
    assert result.status == "validating"
    assert result.identity == "03403791746"
