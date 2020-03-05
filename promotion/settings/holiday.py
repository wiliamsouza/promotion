"""User data store implementation."""
import uuid

from opentelemetry import trace

SERVER = trace.SpanKind.SERVER


class HolidayDataStore:
    """Implements holiday data store interface."""

    def __init__(self, date, tracer):
        self.date = date
        self.tracer = tracer

    # pylint: disable=unused-argument
    def query(self, user_id: uuid.UUID):
        "Query black friday date."
        with self.tracer.start_as_current_span("HolidayDataStore.query", kind=SERVER):
            return self.date
