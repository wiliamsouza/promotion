"""Postgres using SQLAlchemy data store implementation."""
import uuid

from sqlalchemy import Column, Date, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DECIMAL
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    """User SQLAlchemy model"""

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    birthday = Column(Date)
    identity = Column(String)
    email = Column(String)
    name = Column(String)
    password = Column(String)
    orders = relationship("Order", backref="users", order_by="Order.id")


class Order(Base):
    """Order SQLAlchemy model"""

    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    code = Column(UUID(as_uuid=True))
    amount = Column(DECIMAL)
    user_id = Column(ForeignKey('users.id'))
    status = Column(String)
