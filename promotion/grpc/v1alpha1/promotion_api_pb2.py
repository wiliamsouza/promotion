# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: promotion/grpc/v1alpha1/promotion_api.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from promotion.grpc.v1alpha1 import discount_pb2 as promotion_dot_grpc_dot_v1alpha1_dot_discount__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='promotion/grpc/v1alpha1/promotion_api.proto',
  package='promotion.grpc.v1alpha1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n+promotion/grpc/v1alpha1/promotion_api.proto\x12\x17promotion.grpc.v1alpha1\x1a&promotion/grpc/v1alpha1/discount.proto\"?\n\x18RetrievePromotionRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nproduct_id\x18\x02 \x01(\t\"Q\n\x19RetrievePromotionResponse\x12\x34\n\tdiscounts\x18\x01 \x03(\x0b\x32!.promotion.grpc.v1alpha1.Discount2\x8c\x01\n\x0cPromotionAPI\x12|\n\x11RetrievePromotion\x12\x31.promotion.grpc.v1alpha1.RetrievePromotionRequest\x1a\x32.promotion.grpc.v1alpha1.RetrievePromotionResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[promotion_dot_grpc_dot_v1alpha1_dot_discount__pb2.DESCRIPTOR,])




_RETRIEVEPROMOTIONREQUEST = _descriptor.Descriptor(
  name='RetrievePromotionRequest',
  full_name='promotion.grpc.v1alpha1.RetrievePromotionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='promotion.grpc.v1alpha1.RetrievePromotionRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product_id', full_name='promotion.grpc.v1alpha1.RetrievePromotionRequest.product_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=175,
)


_RETRIEVEPROMOTIONRESPONSE = _descriptor.Descriptor(
  name='RetrievePromotionResponse',
  full_name='promotion.grpc.v1alpha1.RetrievePromotionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='discounts', full_name='promotion.grpc.v1alpha1.RetrievePromotionResponse.discounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=258,
)

_RETRIEVEPROMOTIONRESPONSE.fields_by_name['discounts'].message_type = promotion_dot_grpc_dot_v1alpha1_dot_discount__pb2._DISCOUNT
DESCRIPTOR.message_types_by_name['RetrievePromotionRequest'] = _RETRIEVEPROMOTIONREQUEST
DESCRIPTOR.message_types_by_name['RetrievePromotionResponse'] = _RETRIEVEPROMOTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RetrievePromotionRequest = _reflection.GeneratedProtocolMessageType('RetrievePromotionRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEPROMOTIONREQUEST,
  '__module__' : 'promotion.grpc.v1alpha1.promotion_api_pb2'
  # @@protoc_insertion_point(class_scope:promotion.grpc.v1alpha1.RetrievePromotionRequest)
  })
_sym_db.RegisterMessage(RetrievePromotionRequest)

RetrievePromotionResponse = _reflection.GeneratedProtocolMessageType('RetrievePromotionResponse', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEPROMOTIONRESPONSE,
  '__module__' : 'promotion.grpc.v1alpha1.promotion_api_pb2'
  # @@protoc_insertion_point(class_scope:promotion.grpc.v1alpha1.RetrievePromotionResponse)
  })
_sym_db.RegisterMessage(RetrievePromotionResponse)



_PROMOTIONAPI = _descriptor.ServiceDescriptor(
  name='PromotionAPI',
  full_name='promotion.grpc.v1alpha1.PromotionAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=261,
  serialized_end=401,
  methods=[
  _descriptor.MethodDescriptor(
    name='RetrievePromotion',
    full_name='promotion.grpc.v1alpha1.PromotionAPI.RetrievePromotion',
    index=0,
    containing_service=None,
    input_type=_RETRIEVEPROMOTIONREQUEST,
    output_type=_RETRIEVEPROMOTIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROMOTIONAPI)

DESCRIPTOR.services_by_name['PromotionAPI'] = _PROMOTIONAPI

# @@protoc_insertion_point(module_scope)
