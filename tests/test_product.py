"""Tests for product use case implementations."""
import uuid
from unittest import mock

from promotion.product import ProductUseCase


@mock.patch("promotion.postgresql.product.ProductDataStore")
def test_product_exists(store_mock):
    user = mock.MagicMock()
    product = mock.MagicMock()
    percentage = mock.PropertyMock(return_value=5)
    type(product).percentage = percentage
    store_mock.product.return_value = product

    case = ProductUseCase(store_mock)

    result = case.percentage(product.id, user.id)

    assert result == {"percentage": 5}


@mock.patch("promotion.postgresql.product.ProductDataStore")
def test_product_missing(store_mock):
    user = mock.MagicMock()

    store_mock.product.return_value = None
    case = ProductUseCase(store_mock)

    result = case.percentage(uuid.uuid4(), user.id)

    assert result == {"percentage": 0}
