"Interface definitions using python typing."
import datetime
from typing import Dict, List
from typing_extensions import Protocol


class DiscountDataStore(Protocol):
    "Data store interface for discount."

    def __init__(self, database) -> None:
        ...

    def query(self, user_id) -> Dict:
        "Retrieve discount for the given arguments."
        ...


class DiscountUseCase(Protocol):
    "Domain interface for discount bussines logic."

    def __init__(self, store: DiscountDataStore) -> None:
        ...

    def discounts(self, user_id) -> Dict:
        """Retrieve all discounts available."""
        ...


class Promotion(Protocol):
    "Domain interface for promotion bussines logic."

    def __init__(self, discounts: List[DiscountUseCase]) -> None:
        ...

    def promotions(self, user_id) -> Dict:
        """Retrieve all promotions available."""
        ...
