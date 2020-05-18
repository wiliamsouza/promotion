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
    identity: str
    email: str
    name: str
    password: str
    user_id: uuid.UUID = uuid.uuid4()


@dataclasses.dataclass
class Order:
    """Order domain entity"""

    amount: decimal.Decimal
    user: User
    code: uuid.UUID = uuid.uuid4()
    status: str = "In validation"

