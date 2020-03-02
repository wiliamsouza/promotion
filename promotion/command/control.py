"""Control CLI"""
import uuid

import click
import grpc
from google.type.date_pb2 import Date
from prettyconf import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from promotion.grpc.v1alpha1.promotion_api_pb2 import (
    CreateUserRequestResponse, RetrievePromotionRequest)
from promotion.grpc.v1alpha1.promotion_api_pb2_grpc import PromotionAPIStub
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
def list_user():
    """List users."""
    users = session.query(User).all()
    click.echo_via_pager(users)


@client.group("retrieve")
def retrieve():
    """Retrieve commands."""


@retrieve.command("promotion")
@click.option("--user-id", "user_id", required=True, type=click.UUID)
@click.option("--product-id", "product_id", type=click.UUID)
def retrieve_promotion(user_id, product_id):
    """List promotions."""
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = PromotionAPIStub(channel)
        request = RetrievePromotionRequest(
            user_id=str(user_id).encode(), product_id=str(product_id).encode()
        )
        response = stub.RetrievePromotion(request)
    click.echo(response.discounts)


@client.group()
def create():
    """Create commands."""


@create.command("user")
@click.option(
    "--id", "user_id", required=True, type=click.UUID, default=str(uuid.uuid4())
)
@click.option(
    "--birthday", "date", required=True, type=click.DateTime(formats=["%Y-%m-%d"])
)
def create_user(user_id, date):
    """Create user."""

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = PromotionAPIStub(channel)
        birthday = Date(year=date.year, month=date.month, day=date.day)
        request = CreateUserRequestResponse(
            user_id=str(user_id).encode(), date_of_birth=birthday
        )
        response = stub.CreateUser(request)
    click.echo("User:\n{}".format(response))


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
