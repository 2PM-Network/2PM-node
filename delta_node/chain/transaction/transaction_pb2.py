# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transaction.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11transaction.proto\x12\x0btransaction\"\x1e\n\x0bTransaction\x12\x0f\n\x07tx_hash\x18\x01 \x01(\tb\x06proto3')



_TRANSACTION = DESCRIPTOR.message_types_by_name['Transaction']
Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.Transaction)
  })
_sym_db.RegisterMessage(Transaction)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TRANSACTION._serialized_start=34
  _TRANSACTION._serialized_end=64
# @@protoc_insertion_point(module_scope)
