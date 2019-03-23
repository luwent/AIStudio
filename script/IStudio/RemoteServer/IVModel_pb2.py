# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IVModel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='IVModel.proto',
  package='PYIVModel',
  syntax='proto3',
  serialized_options=_b('\n\017io.grpc.IVModelB\007IVModelP\001\242\002\004PYIV'),
  serialized_pb=_b('\n\rIVModel.proto\x12\tPYIVModel\"q\n\x11PTensorShapeProto\x12\x33\n\x03\x64im\x18\x01 \x03(\x0b\x32&.PYIVModel.PTensorShapeProto.Dimension\x1a\'\n\tDimension\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xe6\x02\n\x0cPTensorProto\x12#\n\x05\x64type\x18\x01 \x01(\x0e\x32\x14.PYIVModel.PDataType\x12\x32\n\x0ctensor_shape\x18\x02 \x01(\x0b\x32\x1c.PYIVModel.PTensorShapeProto\x12\x14\n\x08half_val\x18\r \x03(\x05\x42\x02\x10\x01\x12\x15\n\tfloat_val\x18\x05 \x03(\x02\x42\x02\x10\x01\x12\x16\n\ndouble_val\x18\x06 \x03(\x01\x42\x02\x10\x01\x12\x13\n\x07int_val\x18\x07 \x03(\x05\x42\x02\x10\x01\x12\x12\n\nstring_val\x18\x08 \x03(\x0c\x12\x18\n\x0cscomplex_val\x18\t \x03(\x02\x42\x02\x10\x01\x12\x15\n\tint64_val\x18\n \x03(\x03\x42\x02\x10\x01\x12\x14\n\x08\x62ool_val\x18\x0b \x03(\x08\x42\x02\x10\x01\x12\x18\n\x0c\x64\x63omplex_val\x18\x0c \x03(\x01\x42\x02\x10\x01\x12\x16\n\nuint32_val\x18\x10 \x03(\rB\x02\x10\x01\x12\x16\n\nuint64_val\x18\x11 \x03(\x04\x42\x02\x10\x01\"\xbd\x01\n\rPAttrValueDef\x12\x0b\n\x01s\x18\x02 \x01(\x0cH\x00\x12\x0b\n\x01i\x18\x03 \x01(\x03H\x00\x12\x0b\n\x01\x66\x18\x04 \x01(\x02H\x00\x12\x0b\n\x01\x62\x18\x05 \x01(\x08H\x00\x12-\n\x05shape\x18\x06 \x01(\x0b\x32\x1c.PYIVModel.PTensorShapeProtoH\x00\x12)\n\x06tensor\x18\x07 \x01(\x0b\x32\x17.PYIVModel.PTensorProtoH\x00\x12\x15\n\x0bplaceholder\x18\t \x01(\tH\x00\x42\x07\n\x05value\"\xab\x01\n\x08PNodeDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06opname\x18\x02 \x01(\t\x12\r\n\x05input\x18\x03 \x03(\t\x12+\n\x04\x61ttr\x18\x04 \x03(\x0b\x32\x1d.PYIVModel.PNodeDef.AttrEntry\x1a\x45\n\tAttrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.PYIVModel.PAttrValueDef:\x02\x38\x01\".\n\tPGraphDef\x12!\n\x04node\x18\x01 \x03(\x0b\x32\x13.PYIVModel.PNodeDef\"\xbb\x01\n\rPModelMessage\x12\r\n\x05msgID\x18\x01 \x01(\r\x12\x11\n\tbyte_data\x18\x03 \x03(\x0c\x12\x10\n\x08int_data\x18\x04 \x03(\x05\x12\x11\n\tuint_data\x18\x05 \x03(\r\x12\x12\n\nfloat_data\x18\x06 \x03(\x02\x12\x13\n\x0b\x64ouble_data\x18\x07 \x03(\x01\x12\x13\n\x0bstring_data\x18\x08 \x03(\t\x12\x11\n\tbool_data\x18\t \x03(\x08\x12\x12\n\nint64_data\x18\n \x03(\x03*\xf8\x01\n\tPDataType\x12\x0e\n\nDT_INVALID\x10\x00\x12\x0c\n\x08\x44T_FLOAT\x10\x01\x12\r\n\tDT_DOUBLE\x10\x02\x12\x0c\n\x08\x44T_INT32\x10\x03\x12\x0c\n\x08\x44T_UINT8\x10\x04\x12\x0c\n\x08\x44T_INT16\x10\x05\x12\x0b\n\x07\x44T_INT8\x10\x06\x12\r\n\tDT_STRING\x10\x07\x12\x10\n\x0c\x44T_COMPLEX64\x10\x08\x12\x0c\n\x08\x44T_INT64\x10\t\x12\x0b\n\x07\x44T_BOOL\x10\n\x12\r\n\tDT_UINT16\x10\x11\x12\x11\n\rDT_COMPLEX128\x10\x12\x12\x0b\n\x07\x44T_HALF\x10\x13\x12\r\n\tDT_UINT32\x10\x16\x12\r\n\tDT_UINT64\x10\x17\x42#\n\x0fio.grpc.IVModelB\x07IVModelP\x01\xa2\x02\x04PYIVb\x06proto3')
)

_PDATATYPE = _descriptor.EnumDescriptor(
  name='PDataType',
  full_name='PYIVModel.PDataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DT_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_FLOAT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_DOUBLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_INT32', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_UINT8', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_INT16', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_INT8', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_STRING', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_COMPLEX64', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_INT64', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_BOOL', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_UINT16', index=11, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_COMPLEX128', index=12, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_HALF', index=13, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_UINT32', index=14, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_UINT64', index=15, number=23,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1109,
  serialized_end=1357,
)
_sym_db.RegisterEnumDescriptor(_PDATATYPE)

PDataType = enum_type_wrapper.EnumTypeWrapper(_PDATATYPE)
DT_INVALID = 0
DT_FLOAT = 1
DT_DOUBLE = 2
DT_INT32 = 3
DT_UINT8 = 4
DT_INT16 = 5
DT_INT8 = 6
DT_STRING = 7
DT_COMPLEX64 = 8
DT_INT64 = 9
DT_BOOL = 10
DT_UINT16 = 17
DT_COMPLEX128 = 18
DT_HALF = 19
DT_UINT32 = 22
DT_UINT64 = 23



_PTENSORSHAPEPROTO_DIMENSION = _descriptor.Descriptor(
  name='Dimension',
  full_name='PYIVModel.PTensorShapeProto.Dimension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='PYIVModel.PTensorShapeProto.Dimension.size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='PYIVModel.PTensorShapeProto.Dimension.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=102,
  serialized_end=141,
)

_PTENSORSHAPEPROTO = _descriptor.Descriptor(
  name='PTensorShapeProto',
  full_name='PYIVModel.PTensorShapeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dim', full_name='PYIVModel.PTensorShapeProto.dim', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PTENSORSHAPEPROTO_DIMENSION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=141,
)


_PTENSORPROTO = _descriptor.Descriptor(
  name='PTensorProto',
  full_name='PYIVModel.PTensorProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dtype', full_name='PYIVModel.PTensorProto.dtype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor_shape', full_name='PYIVModel.PTensorProto.tensor_shape', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='half_val', full_name='PYIVModel.PTensorProto.half_val', index=2,
      number=13, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_val', full_name='PYIVModel.PTensorProto.float_val', index=3,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_val', full_name='PYIVModel.PTensorProto.double_val', index=4,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_val', full_name='PYIVModel.PTensorProto.int_val', index=5,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_val', full_name='PYIVModel.PTensorProto.string_val', index=6,
      number=8, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scomplex_val', full_name='PYIVModel.PTensorProto.scomplex_val', index=7,
      number=9, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_val', full_name='PYIVModel.PTensorProto.int64_val', index=8,
      number=10, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_val', full_name='PYIVModel.PTensorProto.bool_val', index=9,
      number=11, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dcomplex_val', full_name='PYIVModel.PTensorProto.dcomplex_val', index=10,
      number=12, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint32_val', full_name='PYIVModel.PTensorProto.uint32_val', index=11,
      number=16, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint64_val', full_name='PYIVModel.PTensorProto.uint64_val', index=12,
      number=17, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=144,
  serialized_end=502,
)


_PATTRVALUEDEF = _descriptor.Descriptor(
  name='PAttrValueDef',
  full_name='PYIVModel.PAttrValueDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='PYIVModel.PAttrValueDef.s', index=0,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i', full_name='PYIVModel.PAttrValueDef.i', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='f', full_name='PYIVModel.PAttrValueDef.f', index=2,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='PYIVModel.PAttrValueDef.b', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='PYIVModel.PAttrValueDef.shape', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor', full_name='PYIVModel.PAttrValueDef.tensor', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='placeholder', full_name='PYIVModel.PAttrValueDef.placeholder', index=6,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
    _descriptor.OneofDescriptor(
      name='value', full_name='PYIVModel.PAttrValueDef.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=505,
  serialized_end=694,
)


_PNODEDEF_ATTRENTRY = _descriptor.Descriptor(
  name='AttrEntry',
  full_name='PYIVModel.PNodeDef.AttrEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PYIVModel.PNodeDef.AttrEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='PYIVModel.PNodeDef.AttrEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=799,
  serialized_end=868,
)

_PNODEDEF = _descriptor.Descriptor(
  name='PNodeDef',
  full_name='PYIVModel.PNodeDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PYIVModel.PNodeDef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opname', full_name='PYIVModel.PNodeDef.opname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input', full_name='PYIVModel.PNodeDef.input', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attr', full_name='PYIVModel.PNodeDef.attr', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PNODEDEF_ATTRENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=697,
  serialized_end=868,
)


_PGRAPHDEF = _descriptor.Descriptor(
  name='PGraphDef',
  full_name='PYIVModel.PGraphDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='PYIVModel.PGraphDef.node', index=0,
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
  serialized_start=870,
  serialized_end=916,
)


_PMODELMESSAGE = _descriptor.Descriptor(
  name='PModelMessage',
  full_name='PYIVModel.PModelMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgID', full_name='PYIVModel.PModelMessage.msgID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='byte_data', full_name='PYIVModel.PModelMessage.byte_data', index=1,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_data', full_name='PYIVModel.PModelMessage.int_data', index=2,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint_data', full_name='PYIVModel.PModelMessage.uint_data', index=3,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_data', full_name='PYIVModel.PModelMessage.float_data', index=4,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_data', full_name='PYIVModel.PModelMessage.double_data', index=5,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_data', full_name='PYIVModel.PModelMessage.string_data', index=6,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_data', full_name='PYIVModel.PModelMessage.bool_data', index=7,
      number=9, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_data', full_name='PYIVModel.PModelMessage.int64_data', index=8,
      number=10, type=3, cpp_type=2, label=3,
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
  serialized_start=919,
  serialized_end=1106,
)

_PTENSORSHAPEPROTO_DIMENSION.containing_type = _PTENSORSHAPEPROTO
_PTENSORSHAPEPROTO.fields_by_name['dim'].message_type = _PTENSORSHAPEPROTO_DIMENSION
_PTENSORPROTO.fields_by_name['dtype'].enum_type = _PDATATYPE
_PTENSORPROTO.fields_by_name['tensor_shape'].message_type = _PTENSORSHAPEPROTO
_PATTRVALUEDEF.fields_by_name['shape'].message_type = _PTENSORSHAPEPROTO
_PATTRVALUEDEF.fields_by_name['tensor'].message_type = _PTENSORPROTO
_PATTRVALUEDEF.oneofs_by_name['value'].fields.append(
  _PATTRVALUEDEF.fields_by_name['s'])
_PATTRVALUEDEF.fields_by_name['s'].containing_oneof = _PATTRVALUEDEF.oneofs_by_name['value']
_PATTRVALUEDEF.oneofs_by_name['value'].fields.append(
  _PATTRVALUEDEF.fields_by_name['i'])
_PATTRVALUEDEF.fields_by_name['i'].containing_oneof = _PATTRVALUEDEF.oneofs_by_name['value']
_PATTRVALUEDEF.oneofs_by_name['value'].fields.append(
  _PATTRVALUEDEF.fields_by_name['f'])
_PATTRVALUEDEF.fields_by_name['f'].containing_oneof = _PATTRVALUEDEF.oneofs_by_name['value']
_PATTRVALUEDEF.oneofs_by_name['value'].fields.append(
  _PATTRVALUEDEF.fields_by_name['b'])
_PATTRVALUEDEF.fields_by_name['b'].containing_oneof = _PATTRVALUEDEF.oneofs_by_name['value']
_PATTRVALUEDEF.oneofs_by_name['value'].fields.append(
  _PATTRVALUEDEF.fields_by_name['shape'])
_PATTRVALUEDEF.fields_by_name['shape'].containing_oneof = _PATTRVALUEDEF.oneofs_by_name['value']
_PATTRVALUEDEF.oneofs_by_name['value'].fields.append(
  _PATTRVALUEDEF.fields_by_name['tensor'])
_PATTRVALUEDEF.fields_by_name['tensor'].containing_oneof = _PATTRVALUEDEF.oneofs_by_name['value']
_PATTRVALUEDEF.oneofs_by_name['value'].fields.append(
  _PATTRVALUEDEF.fields_by_name['placeholder'])
_PATTRVALUEDEF.fields_by_name['placeholder'].containing_oneof = _PATTRVALUEDEF.oneofs_by_name['value']
_PNODEDEF_ATTRENTRY.fields_by_name['value'].message_type = _PATTRVALUEDEF
_PNODEDEF_ATTRENTRY.containing_type = _PNODEDEF
_PNODEDEF.fields_by_name['attr'].message_type = _PNODEDEF_ATTRENTRY
_PGRAPHDEF.fields_by_name['node'].message_type = _PNODEDEF
DESCRIPTOR.message_types_by_name['PTensorShapeProto'] = _PTENSORSHAPEPROTO
DESCRIPTOR.message_types_by_name['PTensorProto'] = _PTENSORPROTO
DESCRIPTOR.message_types_by_name['PAttrValueDef'] = _PATTRVALUEDEF
DESCRIPTOR.message_types_by_name['PNodeDef'] = _PNODEDEF
DESCRIPTOR.message_types_by_name['PGraphDef'] = _PGRAPHDEF
DESCRIPTOR.message_types_by_name['PModelMessage'] = _PMODELMESSAGE
DESCRIPTOR.enum_types_by_name['PDataType'] = _PDATATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PTensorShapeProto = _reflection.GeneratedProtocolMessageType('PTensorShapeProto', (_message.Message,), dict(

  Dimension = _reflection.GeneratedProtocolMessageType('Dimension', (_message.Message,), dict(
    DESCRIPTOR = _PTENSORSHAPEPROTO_DIMENSION,
    __module__ = 'IVModel_pb2'
    # @@protoc_insertion_point(class_scope:PYIVModel.PTensorShapeProto.Dimension)
    ))
  ,
  DESCRIPTOR = _PTENSORSHAPEPROTO,
  __module__ = 'IVModel_pb2'
  # @@protoc_insertion_point(class_scope:PYIVModel.PTensorShapeProto)
  ))
_sym_db.RegisterMessage(PTensorShapeProto)
_sym_db.RegisterMessage(PTensorShapeProto.Dimension)

PTensorProto = _reflection.GeneratedProtocolMessageType('PTensorProto', (_message.Message,), dict(
  DESCRIPTOR = _PTENSORPROTO,
  __module__ = 'IVModel_pb2'
  # @@protoc_insertion_point(class_scope:PYIVModel.PTensorProto)
  ))
_sym_db.RegisterMessage(PTensorProto)

PAttrValueDef = _reflection.GeneratedProtocolMessageType('PAttrValueDef', (_message.Message,), dict(
  DESCRIPTOR = _PATTRVALUEDEF,
  __module__ = 'IVModel_pb2'
  # @@protoc_insertion_point(class_scope:PYIVModel.PAttrValueDef)
  ))
_sym_db.RegisterMessage(PAttrValueDef)

PNodeDef = _reflection.GeneratedProtocolMessageType('PNodeDef', (_message.Message,), dict(

  AttrEntry = _reflection.GeneratedProtocolMessageType('AttrEntry', (_message.Message,), dict(
    DESCRIPTOR = _PNODEDEF_ATTRENTRY,
    __module__ = 'IVModel_pb2'
    # @@protoc_insertion_point(class_scope:PYIVModel.PNodeDef.AttrEntry)
    ))
  ,
  DESCRIPTOR = _PNODEDEF,
  __module__ = 'IVModel_pb2'
  # @@protoc_insertion_point(class_scope:PYIVModel.PNodeDef)
  ))
_sym_db.RegisterMessage(PNodeDef)
_sym_db.RegisterMessage(PNodeDef.AttrEntry)

PGraphDef = _reflection.GeneratedProtocolMessageType('PGraphDef', (_message.Message,), dict(
  DESCRIPTOR = _PGRAPHDEF,
  __module__ = 'IVModel_pb2'
  # @@protoc_insertion_point(class_scope:PYIVModel.PGraphDef)
  ))
_sym_db.RegisterMessage(PGraphDef)

PModelMessage = _reflection.GeneratedProtocolMessageType('PModelMessage', (_message.Message,), dict(
  DESCRIPTOR = _PMODELMESSAGE,
  __module__ = 'IVModel_pb2'
  # @@protoc_insertion_point(class_scope:PYIVModel.PModelMessage)
  ))
_sym_db.RegisterMessage(PModelMessage)


DESCRIPTOR._options = None
_PTENSORPROTO.fields_by_name['half_val']._options = None
_PTENSORPROTO.fields_by_name['float_val']._options = None
_PTENSORPROTO.fields_by_name['double_val']._options = None
_PTENSORPROTO.fields_by_name['int_val']._options = None
_PTENSORPROTO.fields_by_name['scomplex_val']._options = None
_PTENSORPROTO.fields_by_name['int64_val']._options = None
_PTENSORPROTO.fields_by_name['bool_val']._options = None
_PTENSORPROTO.fields_by_name['dcomplex_val']._options = None
_PTENSORPROTO.fields_by_name['uint32_val']._options = None
_PTENSORPROTO.fields_by_name['uint64_val']._options = None
_PNODEDEF_ATTRENTRY._options = None
# @@protoc_insertion_point(module_scope)