"""Postgres using SQLAlchemy data store implementation."""
import uuid

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Table, Date
from sqlalchemy import ForeignKey

from sqlalchemy.types import DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

association_table = Table(
    "association",
    Base.metadata,
    Column("product_id", UUID, ForeignKey("products.id")),
    Column("user_id", UUID, ForeignKey("users.id")),
)


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    percentage = Column(DECIMAL)
    users = relationship("User", secondary=association_table, back_populates="products")

    def __repr__(self):
        return "<Product(id={}, percentage='{}')>".format(self.id, self.percentage)


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    birthday = Column(Date)

    products = relationship(
        Product, secondary=association_table, back_populates="users"
    )

    def __repr__(self):
        return "<User(id='{}', birthday='{}')>".format(self.id, self.birthday)
