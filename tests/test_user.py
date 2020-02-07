"""Tests for user use case implementations."""
import datetime
from unittest import mock
from promotion.user import UserUseCase


@mock.patch("promotion.postgresql.user.UserDataStore")
def test_birthday_is_today(store_mock):
    date = datetime.date.today()
    user = mock.MagicMock()
    type(user).birthday = mock.PropertyMock(return_value=date)
    store_mock.user.return_value = user

    case = UserUseCase(store_mock)

    result = case.birthday(user.id)

    assert result == {"percentage": 5}


@mock.patch("promotion.postgresql.user.UserDataStore")
def test_birthday_is_not_today(store_mock):
    date = datetime.datetime.strptime("1981-06-06", "%Y-%m-%d").date()
    user = mock.MagicMock()
    birthday = mock.PropertyMock(return_value=date)
    type(user).birthday = birthday
    store_mock.user.return_value = user

    case = UserUseCase(store_mock)

    result = case.birthday(user.id)

    assert result == {"percentage": 0}
