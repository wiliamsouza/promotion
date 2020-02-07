"""Tests for discount use case implementation."""
import uuid
import datetime
from unittest import mock

from promotion.discount import DiscountUseCase
from promotion.holiday import HolidayUseCase
from promotion.product import ProductUseCase
from promotion.user import UserUseCase


@mock.patch("promotion.postgresql.user.UserDataStore")
@mock.patch("promotion.postgresql.product.ProductDataStore")
def test_discount_only_by_birthday(product_store_mock, user_store_mock):
    date = datetime.date.today()
    user = mock.MagicMock()
    type(user).birthday = mock.PropertyMock(return_value=date)
    user_store_mock.user.return_value = user
    user_case = UserUseCase(user_store_mock)

    date = datetime.datetime.strptime("1970-12-01", "%Y-%m-%d").date()
    holiday_case = HolidayUseCase(date)

    product_store_mock.product.return_value = None
    product_case = ProductUseCase(product_store_mock)

    case = DiscountUseCase(product_case, holiday_case, user_case)

    result = case.discounts(uuid.uuid4(), user.id)

    assert result == {"percentage": 5}


@mock.patch("promotion.postgresql.user.UserDataStore")
@mock.patch("promotion.postgresql.product.ProductDataStore")
def test_discount_only_by_holiday(product_store_mock, user_store_mock):
    user_store_mock.user.return_value = None
    user_case = UserUseCase(user_store_mock)

    date = datetime.date.today()
    holiday_case = HolidayUseCase(date)

    product_store_mock.product.return_value = None
    product_case = ProductUseCase(product_store_mock)

    case = DiscountUseCase(product_case, holiday_case, user_case)

    result = case.discounts(uuid.uuid4(), uuid.uuid4())

    assert result == {"percentage": 10}


@mock.patch("promotion.postgresql.user.UserDataStore")
@mock.patch("promotion.postgresql.product.ProductDataStore")
def test_discount_max(product_store_mock, user_store_mock):
    date = datetime.date.today()
    user = mock.MagicMock()
    type(user).birthday = mock.PropertyMock(return_value=date)
    user_store_mock.user.return_value = user
    user_case = UserUseCase(user_store_mock)

    date = datetime.date.today()
    holiday_case = HolidayUseCase(date)

    product = mock.MagicMock()
    percentage = mock.PropertyMock(return_value=5)
    type(product).percentage = percentage
    product_store_mock.product.return_value = product
    product_case = ProductUseCase(product_store_mock)

    case = DiscountUseCase(product_case, holiday_case, user_case)

    result = case.discounts(product.id, user.id)

    assert result == {"percentage": 10}
