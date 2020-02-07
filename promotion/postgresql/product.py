"""Product data store implementation."""
from promotion.postgresql import Product, User


class ProductDataStore:
    "Implements product data store interface."

    def __init__(self, database):
        self.database = database

    def product(self, product_id, user_id):
        "Query filtering product for the given user and product ID."
        return (
            self.database.query(Product)
            .filter(Product.id == product_id)
            .filter(Product.users.any(User.id == user_id))
            .first()
        )
