# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: header.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import time_pb2 as time__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='header.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_pb=_b('\n\x0cheader.proto\x12\x0bgazebo.msgs\x1a\ntime.proto\"I\n\x06Header\x12\x0e\n\x06str_id\x18\x01 \x01(\t\x12 \n\x05stamp\x18\x02 \x01(\x0b\x32\x11.gazebo.msgs.Time\x12\r\n\x05index\x18\x03 \x01(\x05')
  ,
  dependencies=[time__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='gazebo.msgs.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='str_id', full_name='gazebo.msgs.Header.str_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamp', full_name='gazebo.msgs.Header.stamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='gazebo.msgs.Header.index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=114,
)

_HEADER.fields_by_name['stamp'].message_type = time__pb2._TIME
DESCRIPTOR.message_types_by_name['Header'] = _HEADER

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'header_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Header)
  ))
_sym_db.RegisterMessage(Header)


# @@protoc_insertion_point(module_scope)
