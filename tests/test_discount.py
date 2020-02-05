"""Tests for discount use case implementation."""
import datetime
from unittest.mock import MagicMock, PropertyMock

from promotion.discount import DiscountUseCase
from promotion.holiday import HolidayUseCase
from promotion.user import UserUseCase


def test_discount_only_by_birthday():

    # This mocks the non exist UserDataStore
    date = datetime.date.today()
    user = MagicMock()
    birthday = PropertyMock(return_value=date)
    type(user).date_of_birth = birthday
    user_store = MagicMock()
    user_store.user.return_value = user
    # TODO: Change to use mock.patch after it exists

    user_case = UserUseCase(user_store)

    date = datetime.datetime.strptime("1970-12-01", "%Y-%m-%d").date()
    holiday_case = HolidayUseCase(date)

    store = MagicMock()
    store.discount_product_and_user.return_value = None
    case = DiscountUseCase(store, holiday_case, user_case)

    result = case.discounts(65535, user.id)

    assert result == {"percentage": 5}


def test_discount_only_by_holiday():
    user_store = MagicMock()
    user_store.user.return_value = None
    user_case = UserUseCase(user_store)

    date = datetime.date.today()
    holiday_case = HolidayUseCase(date)

    store = MagicMock()
    store.discount_product_and_user.return_value = None
    case = DiscountUseCase(store, holiday_case, user_case)

    result = case.discounts(65535, 2323)

    assert result == {"percentage": 10}


def test_discount_max():
    # This mocks the non exist UserDataStore
    date = datetime.date.today()
    user = MagicMock()
    birthday = PropertyMock(return_value=date)
    type(user).date_of_birth = birthday
    user_store = MagicMock()
    user_store.user.return_value = user
    # TODO: Change to use mock.patch after it exists
    user_case = UserUseCase(user_store)

    date = datetime.date.today()
    holiday_case = HolidayUseCase(date)

    # This mocks the non exist DiscountDataStore
    discount = MagicMock()
    percentage = PropertyMock(return_value=5)
    type(discount).percentage = percentage
    store = MagicMock()
    store.discount_product_and_user.return_value = discount
    # TODO: Change to use mock.patch after it exists
    case = DiscountUseCase(store, holiday_case, user_case)

    result = case.discounts(discount.product_id, user.id)

    assert result == {"percentage": 10}
