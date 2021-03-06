"""Tests for holiday use case implementation."""
import datetime

from promotion.holiday import HolidayUseCase
from promotion.protocol import DiscountDataStore, DiscountUseCase
from promotion.settings.holiday import HolidayDataStore


def test_black_friday_is_today(tracer):
    date = datetime.date.today()
    store: DiscountDataStore = HolidayDataStore(date, tracer)
    case: DiscountUseCase = HolidayUseCase(store, tracer)

    result = case.discount(None)

    assert result.percentage == 10


def test_black_friday_is_not_today(tracer):
    date = datetime.datetime.strptime("1970-11-25", "%Y-%m-%d").date()
    store: DiscountDataStore = HolidayDataStore(date, tracer)
    case: DiscountUseCase = HolidayUseCase(store, tracer)

    result = case.discount(None)

    assert result.percentage == 0
