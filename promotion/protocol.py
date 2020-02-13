"Interface definitions using python typing."
import uuid
from typing import Any, Dict, List, Protocol, runtime_checkable

from promotion.entity import Discount, Promotion as PromotionEntity


@runtime_checkable
class DiscountDataStore(Protocol):
    """Data store interface for discount."""

    def __init__(self, database) -> None:
        ...

    def query(self, user_id: uuid.UUID) -> Any:
        "Retrieve discount for the given arguments."
        ...


@runtime_checkable
class DiscountUseCase(Protocol):
    """Domain interface for discount bussines logic."""

    store: DiscountDataStore

    def discount(self, user_id: uuid.UUID) -> Discount:
        """Retrieve discount available."""
        ...


@runtime_checkable
class Promotion(Protocol):
    """Domain interface for promotion bussines logic."""

    discounts: List[DiscountUseCase]

    def promotion(self, user_id: uuid.UUID) -> PromotionEntity:
        """Retrieve all promotions available."""
        ...
