"""Entity definition."""
import dataclasses
import datetime
import decimal
from typing import List
import uuid


@dataclasses.dataclass
class Discount:
    percentage: decimal.Decimal


@dataclasses.dataclass
class Promotion:
    discounts: List[Discount]


@dataclasses.dataclass
class User:
    birthday: datetime.date
