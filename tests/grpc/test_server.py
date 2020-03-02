"""Tests for grpc server implementation."""
import datetime
import uuid

from google.type.date_pb2 import Date

from promotion import PromotionUseCase
from promotion.grpc.server import PromotionServicer
from promotion.grpc.v1alpha1.promotion_api_pb2 import (
    CreateUserRequestResponse, RetrievePromotionRequest)
from promotion.holiday import HolidayUseCase
from promotion.postgresql import User
from promotion.postgresql.user import UserDataStore
from promotion.settings.holiday import HolidayDataStore
from promotion.user import UserUseCase

from ..factories import UserFactory


def test_server(database):
    user = UserFactory.create()
    assert database.query(User).one()

    user_store = UserDataStore(database)
    user_case = UserUseCase(user_store)

    date = datetime.date.today()
    holiday_store = HolidayDataStore(date)
    holiday_case = HolidayUseCase(holiday_store)

    case = PromotionUseCase(discounts=[holiday_case, user_case])

    servicer = PromotionServicer(case, user_case)

    request = RetrievePromotionRequest(
        user_id=str(user.id), product_id=str(uuid.uuid4()).encode()
    )
    result = servicer.RetrievePromotion(request, None)

    assert result.discounts[0].pct == 10


def test_server_create_user(database):
    user_store = UserDataStore(database)
    user_case = UserUseCase(user_store)

    date = datetime.datetime.strptime("1970-11-25", "%Y-%m-%d").date()
    holiday_store = HolidayDataStore(date)
    holiday_case = HolidayUseCase(holiday_store)

    case = PromotionUseCase(discounts=[holiday_case, user_case])

    servicer = PromotionServicer(case, user_case)

    date = datetime.date.today()
    birthday = Date(year=date.year, month=date.month, day=date.day)
    user_id = uuid.uuid4()
    request = CreateUserRequestResponse(
        user_id=str(user_id).encode(), date_of_birth=birthday
    )
    result = servicer.CreateUser(request, None)

    assert database.query(User).one()
    assert result.user_id == str(user_id)
    assert result.date_of_birth == birthday
