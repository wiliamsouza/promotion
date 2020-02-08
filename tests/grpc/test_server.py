"""Tests for grpc server implementation."""
import datetime

from promotion.discount import DiscountUseCase
from promotion.holiday import HolidayUseCase
from promotion.product import ProductUseCase
from promotion.user import UserUseCase
from promotion.postgresql.product import ProductDataStore
from promotion.postgresql.user import UserDataStore
from promotion.postgresql import Product as ProductModel, User
from promotion.grpc.server import DiscountServicer
from promotion.grpc.v1alpha1.promotion_api_pb2 import RetrieveDiscountRequest

from ..factories import ProductFactory, UserFactory


def test_server(database):
    user = UserFactory.create()
    assert database.query(User).one()

    product = ProductFactory.create(users=[user])
    assert database.query(ProductModel).one()

    user_store = UserDataStore(database)
    user_case = UserUseCase(user_store)

    date = datetime.date.today()
    holiday_case = HolidayUseCase(date)

    product_store = ProductDataStore(database)
    product_case = ProductUseCase(product_store)

    case = DiscountUseCase(product_case, holiday_case, user_case)

    servicer = DiscountServicer(case)

    request = RetrieveDiscountRequest(
        user_id=str(user.id), product_id=str(product.id).encode()
    )
    result = servicer.RetrieveDiscount(request, None)

    assert result.discounts[0].pct == 10
