"""Tests for order use case implementations."""
import datetime
import uuid
from unittest import mock

from promotion.order import OrderUseCase

from .factories import OrderFactory


@mock.patch("promotion.postgresql.order.OrderDataStore")
def test_place_order(store_mock, tracer):
    user = mock.MagicMock()
    type(user).status = mock.PropertyMock(return_value="validating")
    store_mock.create.return_value = user

    case = OrderUseCase(store_mock, tracer)

    code = uuid.uuid4()
    identity = "03403791746"
    amount = 1000
    date = datetime.date.today()
    result = case.place_order(code, identity, amount, date)

    store_mock.create.assert_called_once_with(code, identity, amount, 'validating', date)

@mock.patch("promotion.postgresql.order.OrderDataStore")
def test_place_order_approved_status(store_mock, tracer):
    user = mock.MagicMock()
    type(user).status = mock.PropertyMock(return_value="approved")
    store_mock.create.return_value = user

    case = OrderUseCase(store_mock, tracer)

    code = uuid.uuid4()
    identity = "15350946056"
    amount = 100
    date = datetime.date.today()
    result = case.place_order(code, identity, amount, date, "nonecziste")

    store_mock.create.assert_called_once_with(code, identity, amount, 'approved', date)

@mock.patch("promotion.postgresql.order.OrderDataStore")
def test_cashback_up_to_a_thousand_100(store_mock, tracer):
    orders = OrderFactory.build_batch(5, amount_cents=10000)
    store_mock.query_all.return_value = orders

    case = OrderUseCase(store_mock, tracer)

    results = case.list_orders_with_cashback()

    assert len(results) == 5
    result = results[0]
    assert result.amount_cashback_cents == 1000
    assert result.cashback_percentage == 10.0
    store_mock.query_all.assert_called()


@mock.patch("promotion.postgresql.order.OrderDataStore")
def test_cashback_up_to_a_thousand(store_mock, tracer):
    orders = OrderFactory.build_batch(5, amount_cents=100000)
    store_mock.query_all.return_value = orders

    case = OrderUseCase(store_mock, tracer)

    results = case.list_orders_with_cashback()

    assert len(results) == 5
    result = results[0]
    assert result.amount_cashback_cents == 10000
    assert result.cashback_percentage == 10.0
    store_mock.query_all.assert_called()


@mock.patch("promotion.postgresql.order.OrderDataStore")
def test_cashback_from_thousand_to_thousand_five_hundred(store_mock, tracer):
    orders = OrderFactory.build_batch(5, amount_cents=150000)
    store_mock.query_all.return_value = orders

    case = OrderUseCase(store_mock, tracer)

    results = case.list_orders_with_cashback()

    assert len(results) == 5
    result = results[0]
    assert result.amount_cashback_cents == 22500
    assert result.cashback_percentage == 15.0
    store_mock.query_all.assert_called()


@mock.patch("promotion.postgresql.order.OrderDataStore")
def test_cashback_more_than_five_hundred(store_mock, tracer):
    orders = OrderFactory.build_batch(5, amount_cents=200000)
    store_mock.query_all.return_value = orders

    case = OrderUseCase(store_mock, tracer)

    results = case.list_orders_with_cashback()

    assert len(results) == 5
    result = results[0]
    assert result.amount_cashback_cents == 40000
    assert result.cashback_percentage == 20.0
    store_mock.query_all.assert_called()
