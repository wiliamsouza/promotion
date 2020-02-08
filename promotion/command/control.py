"""Control CLI"""
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from prettyconf import config
from promotion.postgresql import Base, User

engine = create_engine(config("DATABASE_URL"), echo=True)
Session = sessionmaker(bind=engine)
session = Session()


@click.group()
def cli():
    """Promotion control command line interface."""


@cli.group()
def client():
    """Clients for promotion and user."""


@client.group("list")
def _list():
    """List commands."""


@_list.command("users")
def _list_user():
    """List users."""
    users = session.query(User).all()
    click.echo_via_pager(users)


@client.group()
def create():
    """Create commands."""


@create.command("user")
@click.option(
    "--birthday", "birth", required=True, type=click.DateTime(formats=["%Y-%m-%d"])
)
def create_user(birth):
    """Create user."""
    user = User(birthday=birth)
    session.add(user)
    session.commit()
    click.echo(user)

@cli.group()
def database():
    """Database management commands."""


@database.group("create")
def database_create():
    """Create commands."""


@database_create.command("schema")
def create_schema():
    """Create schemas for all declared models classes."""
    Base.metadata.create_all(engine)
