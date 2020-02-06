"""Tests for user use case implementations."""
import datetime
from unittest.mock import MagicMock, PropertyMock
from promotion.user import UserUseCase


def test_birthday_is_today():

    # This mocks the non exist UserDataStore
    date = datetime.date.today()
    user = MagicMock()
    birthday = PropertyMock(return_value=date)
    type(user).birthday = birthday
    store = MagicMock()
    store.user.return_value = user
    # TODO: Change to use mock.patch after it exists

    case = UserUseCase(store)

    result = case.birthday(user.id)

    assert result == {"percentage": 5}


def test_birthday_is_not_today():

    # This mocks the non exist UserDataStore
    date = datetime.datetime.strptime("1981-06-06", "%Y-%m-%d").date()
    user = MagicMock()
    birthday = PropertyMock(return_value=date)
    type(user).birthday = birthday
    store = MagicMock()
    store.user.return_value = user
    # TODO: Change to use mock.patch after it exists

    case = UserUseCase(store)

    result = case.birthday(user.id)

    assert result == {"percentage": 0}
