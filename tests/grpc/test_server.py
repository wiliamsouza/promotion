"""Tests for grpc server implementation."""
import datetime
import uuid

from promotion.discount import DiscountUseCase
from promotion.holiday import HolidayUseCase
from promotion.user import UserUseCase
from promotion.postgresql.user import UserDataStore
from promotion.postgresql import User
from promotion.grpc.server import PromotionServicer
from promotion.grpc.v1alpha1.promotion_api_pb2 import RetrievePromotionRequest

from ..factories import UserFactory


def test_server(database):
    user = UserFactory.create()
    assert database.query(User).one()

    user_store = UserDataStore(database)
    user_case = UserUseCase(user_store)

    date = datetime.date.today()
    holiday_case = HolidayUseCase(date)

    case = DiscountUseCase(holiday_case, user_case)

    servicer = PromotionServicer(case)

    request = RetrievePromotionRequest(
        user_id=str(user.id), product_id=str(uuid.uuid4()).encode()
    )
    result = servicer.RetrievePromotion(request, None)

    assert result.discounts[0].pct == 10
