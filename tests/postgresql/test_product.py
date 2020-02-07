"""Tests for postgresql product data store implementation."""
from promotion.postgresql.product import Product, ProductDataStore
from promotion.postgresql.user import User

from ..factories import ProductFactory, UserFactory


def test_product_data_store(session):
    user = UserFactory.create()
    assert session.query(User).one()

    product = ProductFactory.create(users=[user])
    assert session.query(Product).one()

    # Create more products to ensure query is working
    ProductFactory.create_batch(5, users=[user])

    store = ProductDataStore(session)

    result = store.product(product.id, user.id)

    assert str(result.id) == str(product.id)
    assert result.percentage == product.percentage
