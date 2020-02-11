"""Promotion API servicer implementation"""
import datetime
from promotion.grpc.v1alpha1.discount_pb2 import Discount
from promotion.grpc.v1alpha1.promotion_api_pb2 import (
    RetrievePromotionResponse,
    CreateUserRequestResponse,
)
from promotion.grpc.v1alpha1.promotion_api_pb2_grpc import PromotionAPIServicer
from promotion.protocol import Promotion
from promotion.user import UserUseCase

from google.type.date_pb2 import Date


class PromotionServicer(PromotionAPIServicer):
    """Implements gRPC product API server"""

    def __init__(
        self, promotion_use_case: Promotion, user_use_case: UserUseCase
    ) -> None:
        self.promotion_use_case = promotion_use_case
        self.user_use_case = user_use_case

    def RetrievePromotion(self, request, context) -> RetrievePromotionResponse:
        discount = self.promotion_use_case.promotions(request.user_id)
        return RetrievePromotionResponse(
            discounts=[Discount(pct=discount["percentage"])]
        )

    def CreateUser(self, request, context) -> CreateUserRequestResponse:
        date = datetime.date(
            request.date_of_birth.year,
            request.date_of_birth.month,
            request.date_of_birth.day,
        )
        user = self.user_use_case.create(request.user_id, date)
        birthday = Date(
            year=user.birthday.year, month=user.birthday.month, day=user.birthday.day
        )
        return CreateUserRequestResponse(user_id=str(user.id), date_of_birth=birthday)
