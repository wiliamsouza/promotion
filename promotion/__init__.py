"Promotion use case implementation."

from promotion import settings


class PromotionUseCase:
    """Implements promotion use case interface."""

    def __init__(self, discounts):
        self.discounts = discounts

    def promotions(self, user_id):
        """Retrieve all promotions available."""
        discount = {"percentage": 0}
        total_percentage = 0

        for d in self.discounts:
            promotion = d.discounts(user_id)
            if promotion:
                total_percentage += promotion["percentage"]

        discount["percentage"] = total_percentage
        if total_percentage > settings.MAX_DISCOUNT_PERCENTAGE:
            discount["percentage"] = settings.MAX_DISCOUNT_PERCENTAGE

        return discount
