"""Daemon CLI"""
from concurrent import futures

import click
import grpc
from opentelemetry import trace
from opentelemetry.ext.jaeger import JaegerSpanExporter
from opentelemetry.sdk.trace import TracerSource
from opentelemetry.sdk.trace.export import (
    SimpleExportSpanProcessor,
    ConsoleSpanExporter,
)
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

    exporter = ConsoleSpanExporter()
    if settings.TRACER_ENDPOINT_HOST and settings.TRACER_ENDPOINT_PORT:
        exporter = JaegerSpanExporter(
            service_name="promotion-grpc",
            agent_host_name=settings.TRACER_ENDPOINT_HOST,
            agent_port=settings.TRACER_ENDPOINT_PORT,
        )

    trace.set_preferred_tracer_source_implementation(lambda T: TracerSource())

    tracer = trace.get_tracer(__name__)

    ## span_processor = BatchExportSpanProcessor(exporter)
    span_processor = SimpleExportSpanProcessor(exporter)

    trace.tracer_source().add_span_processor(span_processor)

    tracer = trace.get_tracer(__name__)

    user_store = UserDataStore(session, tracer)
    user_case = UserUseCase(user_store, tracer)

    holiday_store = HolidayDataStore(settings.BLACK_FRIDAY_DATE, tracer)
    holiday_case = HolidayUseCase(holiday_store, tracer)

    case = PromotionUseCase(discounts=[holiday_case, user_case], tracer=tracer)

    servicer = PromotionServicer(case, user_case, tracer)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service.add_PromotionAPIServicer_to_server(servicer, server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
