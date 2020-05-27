# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from promotion.grpc.v1alpha2 import promotion_api_pb2 as promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2


class PromotionAPIStub(object):
  """PromotionAPI export promotions endpoints.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RetrievePromotion = channel.unary_unary(
        '/promotion.grpc.v1alpha2.PromotionAPI/RetrievePromotion',
        request_serializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.RetrievePromotionRequest.SerializeToString,
        response_deserializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.RetrievePromotionResponse.FromString,
        )
    self.CreateUser = channel.unary_unary(
        '/promotion.grpc.v1alpha2.PromotionAPI/CreateUser',
        request_serializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.CreateUserRequest.SerializeToString,
        response_deserializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.CreateUserResponse.FromString,
        )
    self.CreateOrder = channel.unary_unary(
        '/promotion.grpc.v1alpha2.PromotionAPI/CreateOrder',
        request_serializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.CreateOrderRequestResponse.SerializeToString,
        response_deserializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.CreateOrderRequestResponse.FromString,
        )
    self.ListOrdersWithCashback = channel.unary_unary(
        '/promotion.grpc.v1alpha2.PromotionAPI/ListOrdersWithCashback',
        request_serializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.ListOrderRequest.SerializeToString,
        response_deserializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.ListOrderResponse.FromString,
        )
    self.RetrieveBalance = channel.unary_unary(
        '/promotion.grpc.v1alpha2.PromotionAPI/RetrieveBalance',
        request_serializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.RetrieveBalanceRequest.SerializeToString,
        response_deserializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.RetrieveBalanceResponse.FromString,
        )


class PromotionAPIServicer(object):
  """PromotionAPI export promotions endpoints.
  """

  def RetrievePromotion(self, request, context):
    """RetrievePromotion.
    This retrieve all discounts by product and user IDs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateUser(self, request, context):
    """CreateUser
    This is used to populate user data store.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateOrder(self, request, context):
    """CreateOrder
    This is used to populate order data store.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListOrdersWithCashback(self, request, context):
    """ListOrdersWithCashback
    This is used to list orders along side with cashback information.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RetrieveBalance(self, request, context):
    """RetrieveBalance.
    This retrieve cashback balance .
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PromotionAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RetrievePromotion': grpc.unary_unary_rpc_method_handler(
          servicer.RetrievePromotion,
          request_deserializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.RetrievePromotionRequest.FromString,
          response_serializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.RetrievePromotionResponse.SerializeToString,
      ),
      'CreateUser': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUser,
          request_deserializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.CreateUserRequest.FromString,
          response_serializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.CreateUserResponse.SerializeToString,
      ),
      'CreateOrder': grpc.unary_unary_rpc_method_handler(
          servicer.CreateOrder,
          request_deserializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.CreateOrderRequestResponse.FromString,
          response_serializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.CreateOrderRequestResponse.SerializeToString,
      ),
      'ListOrdersWithCashback': grpc.unary_unary_rpc_method_handler(
          servicer.ListOrdersWithCashback,
          request_deserializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.ListOrderRequest.FromString,
          response_serializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.ListOrderResponse.SerializeToString,
      ),
      'RetrieveBalance': grpc.unary_unary_rpc_method_handler(
          servicer.RetrieveBalance,
          request_deserializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.RetrieveBalanceRequest.FromString,
          response_serializer=promotion_dot_grpc_dot_v1alpha2_dot_promotion__api__pb2.RetrieveBalanceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'promotion.grpc.v1alpha2.PromotionAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
