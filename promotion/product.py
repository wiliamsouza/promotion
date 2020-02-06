"Product use case implementation."


class ProductUseCase:
    """Implements product use case interface."""

    def __init__(self, store):
        self.store = store

    def percentage(self, product_id, user_id):
        discount = {"percentage": 0}
        product = self.store.product(product_id, user_id)
        if product:
            discount["percentage"] = product.percentage

        return discount
