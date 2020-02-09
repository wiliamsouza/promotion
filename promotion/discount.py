"Promotion use case implementation."


class PromotionUseCase:
    """Implements promotion use case interface."""

    def __init__(self, discounts):
        self.discounts = discounts

    def promotions(self, *args, **kwargs):
        """Retrieve all promotions available."""
        discount = {"percentage": 0}
        total_percentage = 0

        for d in self.discounts:
            promotion = d.discounts(args, kwargs)
            if promotion:
                total_percentage += promotion["percentage"]

        discount["percentage"] = total_percentage
        if total_percentage > 10:
            # TODO: Change to get from environment variable
            discount["percentage"] = 10

        return discount
