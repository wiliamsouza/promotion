"""Tests for user use case implementations."""
import datetime
import uuid
from unittest import mock

from promotion.user import UserUseCase

from .factories import UserFactory


@mock.patch("promotion.postgresql.user.UserDataStore")
def test_birthday_is_today(store_mock, tracer):
    date = datetime.date.today()
    user = mock.MagicMock()
    type(user).birthday = mock.PropertyMock(return_value=date)
    store_mock.query.return_value = user

    case = UserUseCase(store_mock, tracer)

    result = case.discount(uuid.uuid4())

    assert result.percentage == 5


@mock.patch("promotion.postgresql.user.UserDataStore")
def test_birthday_month_day(store_mock, tracer):
    today = datetime.date.today()
    date = datetime.datetime.strptime(
        "1970-{}-{}".format(today.month, today.day), "%Y-%m-%d"
    ).date()
    user = mock.MagicMock()
    type(user).birthday = mock.PropertyMock(return_value=date)
    store_mock.query.return_value = user

    case = UserUseCase(store_mock, tracer)

    result = case.discount(uuid.uuid4())

    assert result.percentage == 5


@mock.patch("promotion.postgresql.user.UserDataStore")
def test_birthday_is_not_today(store_mock, tracer):
    date = datetime.datetime.strptime("1981-06-06", "%Y-%m-%d").date()
    user = mock.MagicMock()
    birthday = mock.PropertyMock(return_value=date)
    type(user).birthday = birthday
    store_mock.query.return_value = user

    case = UserUseCase(store_mock, tracer)

    result = case.discount(user.id)

    assert result.percentage == 0


@mock.patch("promotion.postgresql.user.UserDataStore")
def test_create_user_should_hash_password(store_mock, tracer):
    user = UserFactory.build()
    store_mock.create.return_value = user

    case = UserUseCase(store_mock, tracer)

    result = case.create(user.id, user.birthday, user.identity, user.email, user.name, user.password)

    assert 'swordfish' not in store_mock.create.call_args
