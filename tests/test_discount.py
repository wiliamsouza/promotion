"""Tests for discount use case implementation."""
import uuid
import datetime
from unittest import mock

from promotion import PromotionUseCase
from promotion.holiday import HolidayUseCase
from promotion.settings.holiday import HolidayDataStore
from promotion.user import UserUseCase


@mock.patch("promotion.postgresql.user.UserDataStore")
def test_discount_only_by_birthday(user_store_mock):
    date = datetime.date.today()
    user = mock.MagicMock()
    type(user).birthday = mock.PropertyMock(return_value=date)
    user_store_mock.user.return_value = user
    user_case = UserUseCase(user_store_mock)

    date = datetime.datetime.strptime("1970-12-01", "%Y-%m-%d").date()
    holiday_store = HolidayDataStore(date)
    holiday_case = HolidayUseCase(holiday_store)

    case = PromotionUseCase(discounts=[holiday_case, user_case])

    result = case.promotions(user.id)

    assert result == {"percentage": 5}


@mock.patch("promotion.postgresql.user.UserDataStore")
def test_discount_only_by_holiday(user_store_mock):
    user_store_mock.user.return_value = None
    user_case = UserUseCase(user_store_mock)

    date = datetime.date.today()
    store = HolidayDataStore(date)
    holiday_case = HolidayUseCase(store)

    case = PromotionUseCase(discounts=[holiday_case, user_case])

    no_exist = uuid.uuid4()
    result = case.promotions(no_exist)

    assert result == {"percentage": 10}


@mock.patch("promotion.postgresql.user.UserDataStore")
def test_discount_max(user_store_mock):
    date = datetime.date.today()
    user = mock.MagicMock()
    type(user).birthday = mock.PropertyMock(return_value=date)
    user_store_mock.user.return_value = user
    user_case = UserUseCase(user_store_mock)

    date = datetime.date.today()
    store = HolidayDataStore(date)
    holiday_case = HolidayUseCase(store)

    case = PromotionUseCase(discounts=[holiday_case, user_case])

    result = case.promotions(user.id)

    assert result == {"percentage": 10}
