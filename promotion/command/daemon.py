"""Daemon CLI"""
from concurrent import futures

import click
import grpc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from promotion import PromotionUseCase, settings
from promotion.grpc.server import PromotionServicer
from promotion.grpc.v1alpha1 import promotion_api_pb2_grpc as service
from promotion.holiday import HolidayUseCase
from promotion.postgresql.user import UserDataStore
from promotion.settings.holiday import HolidayDataStore
from promotion.user import UserUseCase


@click.group()
def cli():
    """Promotion daemon command line interface."""


@cli.group()
def serve():
    """Start daemon."""


@serve.command("grpc")
def _grpc():
    """Start discount gRPC server."""
    engine = create_engine(settings.DATABASE_URL)
    Session = sessionmaker(bind=engine)
    connection = engine.connect()
    session = Session(bind=connection)

    user_store = UserDataStore(session)
    user_case = UserUseCase(user_store)

    holiday_store = HolidayDataStore(settings.BLACK_FRIDAY_DATE)
    holiday_case = HolidayUseCase(holiday_store)

    case = PromotionUseCase(discounts=[holiday_case, user_case])

    servicer = PromotionServicer(case, user_case)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service.add_PromotionAPIServicer_to_server(servicer, server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
