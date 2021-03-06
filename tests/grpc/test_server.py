"""Tests for grpc server implementation."""
import datetime
import uuid

from google.type.date_pb2 import Date

from argon2 import PasswordHasher

from promotion import settings
from promotion import PromotionUseCase
from promotion.grpc.server import PromotionServicer
from promotion.grpc.v1alpha2.promotion_api_pb2 import (
    CreateUserRequest,
    CreateOrderRequestResponse,
    RetrievePromotionRequest,
    AuthenticateRequest,
)
from promotion.holiday import HolidayUseCase
from promotion.postgresql import User
from promotion.postgresql import Order
from promotion.postgresql.user import UserDataStore
from promotion.postgresql.order import OrderDataStore
from promotion.settings.holiday import HolidayDataStore
from promotion.user import UserUseCase
from promotion.order import OrderUseCase
from promotion.balance import BalanceUseCase, BalanceClient
from promotion.authentication import AuthenticationUseCase

from ..factories import OrderFactory, UserFactory


def test_server_retrieve_promotion(database, tracer):
    user = UserFactory.create()
    assert database.query(User).one()

    user_store = UserDataStore(database, tracer)
    user_case = UserUseCase(user_store, tracer)

    order_store = OrderDataStore(database, tracer)
    order_case = OrderUseCase(order_store, tracer)

    date = datetime.date.today()
    holiday_store = HolidayDataStore(date, tracer)
    holiday_case = HolidayUseCase(holiday_store, tracer)

    balance_client = BalanceClient(settings.BALANCE_TOKEN)
    balance_case = BalanceUseCase(order_case, balance_client, tracer)

    authentication_case = AuthenticationUseCase(user_case, tracer)

    case = PromotionUseCase(discounts=[holiday_case, user_case], tracer=tracer)

    servicer = PromotionServicer(case, user_case, order_case, balance_case, authentication_case, tracer)

    request = RetrievePromotionRequest(
        user_id=str(user.id), product_id=str(uuid.uuid4()).encode()
    )
    result = servicer.RetrievePromotion(request, None)

    assert result.discounts[0].pct == 10


def test_server_create_user(database, tracer):
    user_store = UserDataStore(database, tracer)
    user_case = UserUseCase(user_store, tracer)

    order_store = OrderDataStore(database, tracer)
    order_case = OrderUseCase(order_store, tracer)

    date = datetime.datetime.strptime("1970-11-25", "%Y-%m-%d").date()
    holiday_store = HolidayDataStore(date, tracer)
    holiday_case = HolidayUseCase(holiday_store, tracer)

    balance_client = BalanceClient(settings.BALANCE_TOKEN)
    balance_case = BalanceUseCase(order_case, balance_client, tracer)

    authentication_case = AuthenticationUseCase(user_case, tracer)

    case = PromotionUseCase(discounts=[holiday_case, user_case], tracer=tracer)

    servicer = PromotionServicer(case, user_case, order_case, balance_case, authentication_case, tracer)

    date = datetime.date.today()
    birthday = Date(year=date.year, month=date.month, day=date.day)
    user_id = uuid.uuid4()
    request = CreateUserRequest(
        user_id=str(user_id).encode(),
        date_of_birth=birthday,
        identity="03303441965",
        email="user@email.com",
        name="User name",
        password="swordfish",
    )
    result = servicer.CreateUser(request, None)

    assert database.query(User).one()
    assert result.date_of_birth == birthday
    assert result.identity == "03303441965"
    assert result.email == "user@email.com"
    assert result.name == "User name"
    assert result.user_id == str(user_id)


def test_server_create_order(database, tracer):
    user_store = OrderDataStore(database, tracer)
    user_case = OrderUseCase(user_store, tracer)

    order_store = OrderDataStore(database, tracer)
    order_case = OrderUseCase(order_store, tracer)

    balance_client = BalanceClient(settings.BALANCE_TOKEN)
    balance_case = BalanceUseCase(order_case, balance_client, tracer)

    authentication_case = AuthenticationUseCase(user_case, tracer)

    case = PromotionUseCase(discounts=[], tracer=tracer)

    servicer = PromotionServicer(case, user_case, order_case, balance_case, authentication_case, tracer)

    date = datetime.date.today()
    date = Date(year=date.year, month=date.month, day=date.day)
    order_code = uuid.uuid4()
    request = CreateOrderRequestResponse(
        code=str(order_code).encode(),
        identity="03303441965",
        amount_cents=100,
        status="validating",
        date=date,
    )
    result = servicer.CreateOrder(request, None)

    assert database.query(Order).one()
    assert result.status == "validating"


def test_cashback_from_thousand_to_thousand_five_hundred(database, tracer):
    OrderFactory.create_batch(10, amount_cents=130000)
    assert database.query(Order).count() == 10

    user_store = OrderDataStore(database, tracer)
    user_case = OrderUseCase(user_store, tracer)

    order_store = OrderDataStore(database, tracer)
    order_case = OrderUseCase(order_store, tracer)

    balance_client = BalanceClient(settings.BALANCE_TOKEN)
    balance_case = BalanceUseCase(order_case, balance_client, tracer)

    authentication_case = AuthenticationUseCase(user_case, tracer)

    case = PromotionUseCase(discounts=[], tracer=tracer)

    servicer = PromotionServicer(case, user_case, order_case, balance_case, authentication_case, tracer)

    request = CreateUserRequest()
    response = servicer.ListOrdersWithCashback(request, None)

    assert len(response.orders) == 10
    result = response.orders[0]
    assert result.amount_cashback_cents == 19500
    assert result.cashback_percentage == 15.0


def test_server_authenticate(database, tracer):
    password = "swordfish"
    ph = PasswordHasher()
    password_hash = ph.hash(password)
    user = UserFactory.create(password=password_hash)
    assert database.query(User).one()

    user_store = UserDataStore(database, tracer)
    user_case = UserUseCase(user_store, tracer)

    order_store = OrderDataStore(database, tracer)
    order_case = OrderUseCase(order_store, tracer)

    date = datetime.date.today()
    holiday_store = HolidayDataStore(date, tracer)
    holiday_case = HolidayUseCase(holiday_store, tracer)

    balance_client = BalanceClient(settings.BALANCE_TOKEN)
    balance_case = BalanceUseCase(order_case, balance_client, tracer)

    authentication_case = AuthenticationUseCase(user_case, tracer)

    case = PromotionUseCase(discounts=[holiday_case, user_case], tracer=tracer)

    servicer = PromotionServicer(case, user_case, order_case, balance_case, authentication_case, tracer)

    request = AuthenticateRequest(
        email=user.email,
        password=password
    )
    result = servicer.Authenticate(request, None)

    assert result.id_token.startswith('ey')
