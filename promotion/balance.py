"Cashback balance use case implementation."
import logging
import requests

from opentelemetry import trace

from promotion.entity import Balance

SERVER = trace.SpanKind.SERVER

logger = logging.getLogger(__name__)


class BalanceUseCase:
    """Implements cashback balance."""

    def __init__(self, order_use_case, balance, tracer) -> None:
        self.order = order_use_case
        self.balance_client = balance
        self.tracer = tracer

    def balance(self) -> Balance:
        """Sum the total cashback based on orders approved"""
        with self.tracer.start_as_current_span(
            "BalanceUseCase.balance", kind=SERVER
        ) as span:
            total = 0
            orders = self.order.list_approved_orders()
            for order in orders:
                credit = self.balance_client.cashback_balance_by_identity(
                    order.identity
                )
                total += credit
            span.set_attribute("total_balance_amount", str(total))
            return Balance(total_amount=total)


class TokenAuth(requests.auth.AuthBase):
    """Token based header authentication."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["Authorization"] = "token {}".format(self.token)
        return r


class BalanceClient:
    """HTTP client for balance API"""

    def __init__(self, token):
        self.auth = TokenAuth(token)
        self.url = (
            "https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf={}"
        )

    def cashback_balance_by_identity(self, identity):
        """Cashback balance by identity."""
        response = requests.get(self.url.format(identity), auth=self.auth)
        if response.status_code == 200:
            return response.json()["body"]["credit"]
        return None
