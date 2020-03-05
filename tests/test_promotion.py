"""Tests for discount use case implementation."""
import datetime
import uuid
from unittest import mock

from promotion import PromotionUseCase
from promotion.holiday import HolidayUseCase
from promotion.settings.holiday import HolidayDataStore
from promotion.user import UserUseCase


@mock.patch("promotion.postgresql.user.UserDataStore")
def test_discount_only_by_birthday(user_store_mock, tracer):
    date = datetime.date.today()
    user = mock.MagicMock()
    type(user).birthday = mock.PropertyMock(return_value=date)
    user_store_mock.query.return_value = user
    user_case = UserUseCase(user_store_mock, tracer)

    date = datetime.datetime.strptime("1970-12-01", "%Y-%m-%d").date()
    holiday_store = HolidayDataStore(date, tracer)
    holiday_case = HolidayUseCase(holiday_store, tracer)

    case = PromotionUseCase(discounts=[holiday_case, user_case], tracer=tracer)

    result = case.promotion(uuid.uuid4())

    assert result.discounts[0].percentage == 5


@mock.patch("promotion.postgresql.user.UserDataStore")
def test_discount_only_by_holiday(user_store_mock, tracer):
    user_store_mock.user.return_value = None
    user_case = UserUseCase(user_store_mock, tracer)

    date = datetime.date.today()
    store = HolidayDataStore(date, tracer)
    holiday_case = HolidayUseCase(store, tracer)

    case = PromotionUseCase(discounts=[holiday_case, user_case], tracer=tracer)

    no_exist = uuid.uuid4()
    result = case.promotion(no_exist)

    assert result.discounts[0].percentage == 10


@mock.patch("promotion.postgresql.user.UserDataStore")
def test_discount_max(user_store_mock, tracer):
    date = datetime.date.today()
    user = mock.MagicMock()
    type(user).birthday = mock.PropertyMock(return_value=date)
    user_store_mock.user.return_value = user
    user_case = UserUseCase(user_store_mock, tracer)

    date = datetime.date.today()
    store = HolidayDataStore(date, tracer)
    holiday_case = HolidayUseCase(store, tracer)

    case = PromotionUseCase(discounts=[holiday_case, user_case], tracer=tracer)

    result = case.promotion(user.id)

    assert result.discounts[0].percentage == 10
