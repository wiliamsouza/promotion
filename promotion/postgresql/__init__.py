"""Postgres using SQLAlchemy data store implementation."""
import uuid

from sqlalchemy import Column, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """User SQLAlchemy model"""

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    birthday = Column(Date)
