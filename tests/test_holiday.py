"""Tests for holiday use case implementation."""
import datetime

from promotion.holiday import HolidayUseCase


def test_black_friday_is_today():
    date = datetime.date.today()
    holiday = HolidayUseCase(date)

    result = holiday.black_friday()

    assert result == {"percentage": 10}


def test_black_friday_is_not_today():
    date = datetime.datetime.strptime("1970-11-25", "%Y-%m-%d").date()
    holiday = HolidayUseCase(date)

    result = holiday.black_friday()

    assert result == {"percentage": 0}
