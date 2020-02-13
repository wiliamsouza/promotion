"""Tests for holiday use case implementation."""
import datetime

from promotion.holiday import HolidayUseCase
from promotion.protocol import DiscountUseCase, DiscountDataStore
from promotion.settings.holiday import HolidayDataStore


def test_black_friday_is_today():
    date = datetime.date.today()
    store: DiscountDataStore = HolidayDataStore(date)
    case: DiscountUseCase = HolidayUseCase(store)

    result = case.discount(None)

    assert result.percentage == 10


def test_black_friday_is_not_today():
    date = datetime.datetime.strptime("1970-11-25", "%Y-%m-%d").date()
    store: DiscountDataStore = HolidayDataStore(date)
    case: DiscountUseCase = HolidayUseCase(store)

    result = case.discount(None)

    assert result.percentage == 0
