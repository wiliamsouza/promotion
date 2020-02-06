"""Tests for product use case implementations."""
import uuid
from unittest.mock import MagicMock, PropertyMock

from promotion.product import ProductUseCase


def test_product_exists():
    user = MagicMock()

    product = MagicMock()
    percentage = PropertyMock(return_value=5)
    type(product).percentage = percentage
    store = MagicMock()
    store.product.return_value = product
    case = ProductUseCase(store)

    result = case.percentage(product.id, user.id)

    assert result == {"percentage": 5}


def test_product_missing():
    user = MagicMock()

    store = MagicMock()
    store.product.return_value = None
    case = ProductUseCase(store)

    result = case.percentage(uuid.uuid4(), user.id)

    assert result == {"percentage": 0}
