"""Tests for postgresql user data store implementation."""
import datetime
import uuid

from promotion.postgresql.user import UserDataStore
from promotion.postgresql import User

from ..factories import UserFactory


def test_query_user_data_store(database, tracer):
    uid = uuid.uuid4()
    user = UserFactory.create(id=uid)
    assert database.query(User).one()
    store = UserDataStore(database, tracer)

    result = store.query(user.id)

    assert result.user_id == user.id
    assert result.birthday == datetime.date.today()
    assert result.identity == user.identity
    assert result.email == user.email
    assert result.name == user.name
    # TODO: Change it to be a secure password hash
    assert result.password == user.password
