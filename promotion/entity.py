"""Entity definition."""
import dataclasses
import datetime
import decimal
import uuid
from typing import List


@dataclasses.dataclass
class Balance:
    """Balance domain entity"""

    total_amount: int


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
    identity: str
    email: str
    name: str
    # TODO: Remove this from here.
    password: str
    user_id: uuid.UUID = uuid.uuid4()


@dataclasses.dataclass
class Order:
    """Order domain entity"""

    amount_cents: int
    code: uuid.UUID
    date: datetime.date
    identity: str
    status: str = "validating"
    amount_cashback_cents: int = 0
    cashback_percentage: float = 0.0
