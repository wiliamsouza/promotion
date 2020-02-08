"""Discount API servicer implementation"""
from promotion.grpc.v1alpha1.discount_pb2 import Discount
from promotion.grpc.v1alpha1.promotion_api_pb2 import RetrieveDiscountResponse
from promotion.grpc.v1alpha1.promotion_api_pb2_grpc import DiscountAPIServicer
from promotion import DiscountUseCase


class DiscountServicer(DiscountAPIServicer):
    """Implements gRPC product API server"""

    def __init__(self, use_case: DiscountUseCase) -> None:
        self.use_case = use_case

    def RetrieveDiscount(self, request, context):
        discount = self.use_case.discounts(request.product_id, request.user_id)
        return RetrieveDiscountResponse(
            discounts=[Discount(pct=discount["percentage"])]
        )
