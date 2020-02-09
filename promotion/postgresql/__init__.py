"""Postgres using SQLAlchemy data store implementation."""
import uuid

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Table, Date
from sqlalchemy import ForeignKey

from sqlalchemy.types import DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    birthday = Column(Date)
