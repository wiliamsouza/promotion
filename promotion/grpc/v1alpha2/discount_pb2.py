# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: promotion/grpc/v1alpha2/discount.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='promotion/grpc/v1alpha2/discount.proto',
  package='promotion.grpc.v1alpha2',
  syntax='proto3',
  serialized_options=b'Z\010v1alpha2',
  serialized_pb=b'\n&promotion/grpc/v1alpha2/discount.proto\x12\x17promotion.grpc.v1alpha2\"\x17\n\x08\x44iscount\x12\x0b\n\x03pct\x18\x01 \x01(\x02\x42\nZ\x08v1alpha2b\x06proto3'
)




_DISCOUNT = _descriptor.Descriptor(
  name='Discount',
  full_name='promotion.grpc.v1alpha2.Discount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pct', full_name='promotion.grpc.v1alpha2.Discount.pct', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=67,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['Discount'] = _DISCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Discount = _reflection.GeneratedProtocolMessageType('Discount', (_message.Message,), {
  'DESCRIPTOR' : _DISCOUNT,
  '__module__' : 'promotion.grpc.v1alpha2.discount_pb2'
  # @@protoc_insertion_point(class_scope:promotion.grpc.v1alpha2.Discount)
  })
_sym_db.RegisterMessage(Discount)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)