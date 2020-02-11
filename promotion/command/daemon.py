"""Daemon CLI"""
import datetime
from concurrent import futures

import click

import grpc

from prettyconf import config

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from promotion.grpc.v1alpha1 import promotion_api_pb2_grpc as service
from promotion.grpc.server import PromotionServicer
from promotion import PromotionUseCase
from promotion.holiday import HolidayUseCase
from promotion.user import UserUseCase
from promotion.postgresql.user import UserDataStore


@click.group()
def cli():
    """Promotion daemon command line interface."""


@cli.group()
def serve():
    """Start daemon."""


@serve.command("grpc")
def _grpc():
    """Start discount gRPC server."""
    engine = create_engine(config("DATABASE_URL"))
    Session = sessionmaker(bind=engine)
    connection = engine.connect()
    session = Session(bind=connection)

    user_store = UserDataStore(session)
    user_case = UserUseCase(user_store)

    date = datetime.date.today()
    holiday_case = HolidayUseCase(date)

    case = PromotionUseCase(discounts=[holiday_case, user_case])

    servicer = PromotionServicer(case, user_case)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service.add_PromotionAPIServicer_to_server(servicer, server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
