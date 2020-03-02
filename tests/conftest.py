import pytest
from prettyconf import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from promotion import settings
from promotion.postgresql import Base

from .factories import UserFactory

engine = create_engine(settings.TEST_DATABASE_URL, echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


@pytest.fixture(scope="module")
def connection():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture(scope="function")
def database(connection):
    transaction = connection.begin()
    session = Session(bind=connection)
    UserFactory._meta.sqlalchemy_session = session
    yield session
    session.close()
    transaction.rollback()
