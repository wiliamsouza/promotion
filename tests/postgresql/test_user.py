"""Tests for postgresql user data store implementation."""
import datetime

from promotion.postgresql.user import UserDataStore
from promotion.postgresql import User

from ..factories import UserFactory


def test_user_data_store(database, tracer):
    user = UserFactory.create()
    assert database.query(User).one()
    store = UserDataStore(database, tracer)

    result = store.query(user.id)

    assert result.birthday == datetime.date.today()
