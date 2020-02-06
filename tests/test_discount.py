"""Tests for discount use case implementation."""
import uuid
import datetime
from unittest.mock import MagicMock, PropertyMock

from promotion.discount import DiscountUseCase
from promotion.holiday import HolidayUseCase
from promotion.product import ProductUseCase
from promotion.user import UserUseCase


def test_discount_only_by_birthday():

    # This mocks the non exist UserDataStore
    date = datetime.date.today()
    user = MagicMock()
    birthday = PropertyMock(return_value=date)
    type(user).birthday = birthday
    user_store = MagicMock()
    user_store.user.return_value = user
    user_case = UserUseCase(user_store)

    date = datetime.datetime.strptime("1970-12-01", "%Y-%m-%d").date()
    holiday_case = HolidayUseCase(date)

    product_store = MagicMock()
    product_store.product.return_value = None
    product_case = ProductUseCase(product_store)
    # TODO: Change to use mock.patch after it exists
    case = DiscountUseCase(product_case, holiday_case, user_case)

    result = case.discounts(uuid.uuid4(), user.id)

    assert result == {"percentage": 5}


def test_discount_only_by_holiday():

    # This mocks the non exist UserDataStore
    user_store = MagicMock()
    user_store.user.return_value = None
    user_case = UserUseCase(user_store)

    date = datetime.date.today()
    holiday_case = HolidayUseCase(date)

    product_store = MagicMock()
    product_store.product.return_value = None
    product_case = ProductUseCase(product_store)
    # TODO: Change to use mock.patch after it exists
    case = DiscountUseCase(product_case, holiday_case, user_case)

    result = case.discounts(uuid.uuid4(), uuid.uuid4())

    assert result == {"percentage": 10}


def test_discount_max():
    # This mocks the non exist UserDataStore
    date = datetime.date.today()
    user = MagicMock()
    birthday = PropertyMock(return_value=date)
    type(user).birthday = birthday
    user_store = MagicMock()
    user_store.user.return_value = user
    # TODO: Change to use mock.patch after it exists
    user_case = UserUseCase(user_store)

    date = datetime.date.today()
    holiday_case = HolidayUseCase(date)

    product = MagicMock()
    percentage = PropertyMock(return_value=5)
    type(product).percentage = percentage
    product_store = MagicMock()
    product_store.product.return_value = product
    product_case = ProductUseCase(product_store)

    # TODO: Change to use mock.patch after it exists
    case = DiscountUseCase(product_case, holiday_case, user_case)

    result = case.discounts(product.id, user.id)

    assert result == {"percentage": 10}
