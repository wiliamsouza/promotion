"Discount use case implementation."


class DiscountUseCase:
    """Implements discount use case interface."""

    def __init__(self, holiday, user):
        self.holiday = holiday
        self.user = user

    def discounts(self, product_id, user_id):
        """Retrieve all discounts available.

        Use cases implemented:

        * User birthday
        * Black friday holiday
        """
        discount = {"percentage": 0}
        total_percentage = 0

        by_birthday = self.user.birthday(user_id)
        if by_birthday:
            total_percentage += by_birthday["percentage"]

        by_holiday = self.holiday.black_friday()
        if by_holiday:
            total_percentage += by_holiday["percentage"]

        discount["percentage"] = total_percentage
        if total_percentage > 10:
            # TODO: Change to get from environment variable
            discount["percentage"] = 10

        return discount
