"""Promotion API servicer implementation"""
from promotion.grpc.v1alpha1.discount_pb2 import Discount
from promotion.grpc.v1alpha1.promotion_api_pb2 import RetrievePromotionResponse
from promotion.grpc.v1alpha1.promotion_api_pb2_grpc import PromotionAPIServicer
from promotion import Promotion


class PromotionServicer(PromotionAPIServicer):
    """Implements gRPC product API server"""

    def __init__(self, use_case: Promotion) -> None:
        self.use_case = use_case

    def RetrievePromotion(self, request, context):
        discount = self.use_case.promotions(request.user_id)
        return RetrievePromotionResponse(
            discounts=[Discount(pct=discount["percentage"])]
        )
