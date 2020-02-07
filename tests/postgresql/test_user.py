"""Tests for postgresql user data store implementation."""
import datetime

from promotion.postgresql.user import User, UserDataStore

from ..factories import UserFactory


def test_user_data_store(session):
    user = UserFactory.create()
    assert session.query(User).one()
    store = UserDataStore(session)

    result = store.user(user.id)

    assert result.birthday == datetime.date.today()
