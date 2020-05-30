"""Promotion API servicer implementation"""
import datetime

from google.type.date_pb2 import Date
from opentelemetry import trace

from promotion.grpc.v1alpha2.discount_pb2 import Discount
from promotion.grpc.v1alpha2.promotion_api_pb2 import (
    CreateOrderRequestResponse,
    CreateUserResponse,
    RetrievePromotionResponse,
    ListOrderResponse,
    Order,
    RetrieveBalanceResponse,
    AuthenticateResponse,
)
from promotion.grpc.v1alpha2.promotion_api_pb2_grpc import PromotionAPIServicer
from promotion.protocol import Promotion
from promotion.user import UserUseCase
from promotion.order import OrderUseCase

SERVER = trace.SpanKind.SERVER


class PromotionServicer(PromotionAPIServicer):
    """Implements gRPC product API server"""

    def __init__(self, promotion_use_case: Promotion,
                 user_use_case: UserUseCase, order_use_case: OrderUseCase,
                 balance_use_case, authentication_use_case, tracer
                 ):
        self.balance_use_case = balance_use_case
        self.promotion_use_case = promotion_use_case
        self.user_use_case = user_use_case
        self.order_use_case = order_use_case
        self.tracer = tracer
        self.authentication_use_case = authentication_use_case

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

            user = self.user_use_case.create(
                request.user_id,
                date,
                request.identity,
                request.email,
                request.name,
                request.password
            )

            birthday = Date(
                year=user.birthday.year,
                month=user.birthday.month,
                day=user.birthday.day,
            )

            return CreateUserResponse(
                user_id=str(user.user_id),
                date_of_birth=birthday,
                identity=user.identity,
                email=user.email,
                name=user.name,
            )

    def CreateOrder(self, request, context):
        with self.tracer.start_as_current_span(
            "PromotionServicer.CreateOrder", kind=SERVER
        ):
            date = datetime.date(
                request.date.year,
                request.date.month,
                request.date.day,
            )

            order = self.order_use_case.place_order(
                request.code,
                request.identity,
                request.amount_cents,
                date,
                request.status,
            )

            order_date = Date(
                year=order.date.year,
                month=order.date.month,
                day=order.date.day,
            )
            return CreateOrderRequestResponse(
                code=str(order.code),
                identity=order.identity,
                amount_cents=order.amount_cents,
                status=order.status,
                date=order_date,
            )

    def ListOrdersWithCashback(self, request, context):
        with self.tracer.start_as_current_span(
            "PromotionServicer.ListOrdersWithCashback", kind=SERVER
        ):
            cashbacks = []
            orders = self.order_use_case.list_orders_with_cashback()
            for order in orders:
                order_date = Date(
                    year=order.date.year,
                    month=order.date.month,
                    day=order.date.day,
                )
                cashbacks.append(
                    Order(
                        amount_cents=order.amount_cents,
                        amount_cashback_cents=order.amount_cashback_cents,
                        code=str(order.code),
                        cashback_percentage=order.cashback_percentage,
                        date=order_date,
                        identity=order.identity,
                        status=order.status,
                    )
                )
            return ListOrderResponse(orders=cashbacks)

    def RetrieveBalance(self, request, context):
        with self.tracer.start_as_current_span(
            "PromotionServicer.RetrieveBalance", kind=SERVER
        ):

            balance = self.balance_use_case.balance()
            return RetrieveBalanceResponse(balance=balance.total_amount)

    def Authenticate(self, request, context):
        with self.tracer.start_as_current_span(
            "PromotionServicer.Authenticate", kind=SERVER
        ):

            id_token = self.authentication_use_case.authenticate(request.email, request.password)
            return AuthenticateResponse(id_token=id_token)
