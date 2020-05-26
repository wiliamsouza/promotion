"""Tests for postgresql order data store implementation."""
import datetime
import uuid

from promotion.postgresql.order import OrderDataStore
from promotion.postgresql import Order

from ..factories import OrderFactory


def test_query_order_data_store(database, tracer):
    order = OrderFactory.create()
    assert database.query(Order).one()
    store = OrderDataStore(database, tracer)

    result = store.query(order.code)

    assert result.date == datetime.date.today()
    assert result.amount_cents == 9990
    assert result.status == "validating"
    assert result.identity == "03403791746"


def test_query_all_order_data_store(database, tracer):
    OrderFactory.create_batch(10)
    assert database.query(Order).count() == 10
    store = OrderDataStore(database, tracer)

    result = store.query_all()

    assert len(result) == 10


def test_create_order_data_store(database, tracer):
    assert database.query(Order).one_or_none() is None
    store = OrderDataStore(database, tracer)

    code = uuid.uuid4()
    today = datetime.date.today()
    result = store.create(
        code=code,
        identity="13723774968",
        amount_cents=9099,
        status="validating",
        date=today,
    )

    assert result.date == datetime.date.today()
    assert result.amount_cents == 9099
    assert result.status == "validating"
    assert result.identity == "13723774968"
