"Interface definitions using python typing."
import datetime
from typing import Dict
from typing_extensions import Protocol


class ProductDataStore(Protocol):
    "Data store interface for products."

    def __init__(self, database) -> None:
        ...

    def product(self, product_id, user_id) -> Dict:
        "Retrieve product for the given product and user ID."
        ...


class UserDataStore(Protocol):
    "Data store interface for users."

    def __init__(self, database) -> None:
        ...

    def user(self, user_id) -> Dict:
        "Retrieve user for the given ID."
        ...


class DiscountUseCase(Protocol):
    "Domain interface for discount bussines logic."

    def __init__(
        self, product: "ProductUseCase", holiday: "HolidayUseCase", user: "UserUseCase"
    ) -> None:
        ...

    def discounts(self, product_id, user_id) -> Dict:
        """Retrieve all discounts available."""
        ...


class HolidayUseCase(Protocol):
    """Domain interface for discount by holiday bussines logic."""

    def __init__(self, date: datetime.date) -> None:
        ...

    def black_friday(self) -> Dict:
        """Give discount if it is black friday."""
        ...


class ProductUseCase(Protocol):
    "Domain interface for discount by product and user bussines logic."

    def __init__(self, store: ProductDataStore) -> None:
        ...

    def percentage(self, product_id, user_id) -> Dict:
        """Give discount by product and user combination."""
        ...


class UserUseCase(Protocol):
    "Domain interface for discount by user bussines logic."

    def __init__(self, store: UserDataStore) -> None:
        ...

    def birthday(self, user_id) -> Dict:
        """Give discount if is the exact date a person was born."""
        ...
