"""Entity definition."""
import dataclasses
import datetime
import decimal
import uuid
from typing import List


@dataclasses.dataclass
class Discount:
    """Discount domain entity"""

    percentage: decimal.Decimal


@dataclasses.dataclass
class Promotion:
    """Promotion domain entity"""

    discounts: List[Discount]


@dataclasses.dataclass
class User:
    """User domain entity"""

    birthday: datetime.date
    user_id: uuid.UUID = uuid.uuid4()
