"""Tests for order use case implementations."""
import datetime
import uuid
from unittest import mock

from promotion.order import OrderUseCase


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
