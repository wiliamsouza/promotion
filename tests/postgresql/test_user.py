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


def test_query_user_by_email(database, tracer):
    email = 'jane@doe.com'
    user = UserFactory.create(email=email)
    assert database.query(User).one()
    store = UserDataStore(database, tracer)

    result = store.query_by_email(user.email)

    assert str(result.user_id) == user.id
    assert result.birthday == datetime.date.today()
    assert result.identity == user.identity
    assert result.email == user.email
    assert result.name == user.name
    # TODO: Change it to be a secure password hash
    assert result.password == user.password


def test_create_user_data_store(database, tracer):
    assert database.query(User).one_or_none() is None
    store = UserDataStore(database, tracer)

    uid = uuid.uuid4()
    result = store.create(
        uid,
        datetime.date.today(),
        "13723774968",
        "jane@doe.com",
        "Jane Doe",
        "swordfish"
    )

    assert result.user_id == uid
    assert result.birthday == datetime.date.today()
    assert result.identity == "13723774968"
    assert result.email == "jane@doe.com"
    assert result.name == "Jane Doe"
    # TODO: Change it to be a secure password hash
    assert result.password == "swordfish"
