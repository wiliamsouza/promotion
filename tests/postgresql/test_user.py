"""Tests for postgresql user data store implementation."""
import datetime

from promotion.postgresql.user import User, UserDataStore

from ..factories import UserFactory


def test_user_data_store(database):
    user = UserFactory.create()
    assert database.query(User).one()
    store = UserDataStore(database)

    result = store.query(user.id)

    assert result.birthday == datetime.date.today()
