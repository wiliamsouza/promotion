"Promotion use case implementation."
import uuid
from decimal import Decimal
from typing import List

from opentelemetry import trace

from promotion import settings
from promotion.entity import Discount, Promotion
from promotion.protocol import DiscountUseCase

SERVER = trace.SpanKind.SERVER


class PromotionUseCase:
    """Implements Promotion use case interface."""

    def __init__(self, discounts: List[DiscountUseCase], tracer) -> None:
        self.discounts = discounts
        self.tracer = tracer

    def promotion(self, user_id: uuid.UUID) -> Promotion:
        """ Promotion iterate discounts use cases.

        Sum each discount percentage and compare with the configured maximun.

        Args:
            user_id: User idenmtifier

        Returns:
            instance: :class:`promotion.entity.Promotion`
        """
        with self.tracer.start_as_current_span(
            "PromotionUseCase.promotion", kind=SERVER
        ) as span:
            total_discount = Discount(percentage=Decimal(0))
            total_percentage = Decimal(0)
            # span.set_attribute("discounts_list", ",".join(self.discounts))
            for d in self.discounts:
                discount = d.discount(user_id)
                if discount:
                    total_percentage += discount.percentage

            total_discount.percentage = total_percentage
            if total_percentage > settings.MAX_DISCOUNT_PERCENTAGE:
                total_discount.percentage = settings.MAX_DISCOUNT_PERCENTAGE

            span.set_attribute(
                "given_discount_percentage", str(total_discount.percentage)
            )
            return Promotion(discounts=[total_discount])
