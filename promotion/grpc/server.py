"""Promotion API servicer implementation"""
import datetime

from google.type.date_pb2 import Date
from opentelemetry import trace

from promotion.grpc.v1alpha1.discount_pb2 import Discount
from promotion.grpc.v1alpha1.promotion_api_pb2 import (
    CreateUserRequestResponse,
    RetrievePromotionResponse,
)
from promotion.grpc.v1alpha1.promotion_api_pb2_grpc import PromotionAPIServicer
from promotion.protocol import Promotion
from promotion.user import UserUseCase

SERVER = trace.SpanKind.SERVER


class PromotionServicer(PromotionAPIServicer):
    """Implements gRPC product API server"""

    def __init__(
        self, promotion_use_case: Promotion, user_use_case: UserUseCase, tracer
    ):
        self.promotion_use_case = promotion_use_case
        self.user_use_case = user_use_case
        self.tracer = tracer

    def RetrievePromotion(self, request, context):
        with self.tracer.start_as_current_span(
            "PromotionServicer.RetrievePromotion", kind=SERVER
        ):

            promotion = self.promotion_use_case.promotion(request.user_id)
            discounts = []
            for discount in promotion.discounts:
                discounts.append(Discount(pct=float(discount.percentage)))

            return RetrievePromotionResponse(discounts=discounts)

    def CreateUser(self, request, context):
        with self.tracer.start_as_current_span(
            "PromotionServicer.CreateUser", kind=SERVER
        ):

            date = datetime.date(
                request.date_of_birth.year,
                request.date_of_birth.month,
                request.date_of_birth.day,
            )
            user = self.user_use_case.create(request.user_id, date)
            birthday = Date(
                year=user.birthday.year,
                month=user.birthday.month,
                day=user.birthday.day,
            )
            return CreateUserRequestResponse(
                user_id=str(user.user_id), date_of_birth=birthday
            )
