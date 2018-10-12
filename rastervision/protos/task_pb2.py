# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/task.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from rastervision.protos import class_item_pb2 as rastervision_dot_protos_dot_class__item__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/task.proto',
  package='rv.protos',
  syntax='proto2',
  serialized_pb=_b('\n\x1erastervision/protos/task.proto\x12\trv.protos\x1a$rastervision/protos/class_item.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x80\x0b\n\nTaskConfig\x12\x11\n\ttask_type\x18\x01 \x02(\t\x12\x1e\n\x12predict_batch_size\x18\x02 \x01(\x05:\x02\x31\x30\x12\x1b\n\x13predict_package_uri\x18\x03 \x01(\t\x12\x13\n\x05\x64\x65\x62ug\x18\x04 \x01(\x08:\x04true\x12\x19\n\x11predict_debug_uri\x18\x05 \x01(\t\x12N\n\x17object_detection_config\x18\x06 \x01(\x0b\x32+.rv.protos.TaskConfig.ObjectDetectionConfigH\x00\x12T\n\x1a\x63hip_classification_config\x18\x07 \x01(\x0b\x32..rv.protos.TaskConfig.ChipClassificationConfigH\x00\x12X\n\x1csemantic_segmentation_config\x18\x08 \x01(\x0b\x32\x30.rv.protos.TaskConfig.SemanticSegmentationConfigH\x00\x12\x30\n\rcustom_config\x18\t \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x1a\xb2\x03\n\x15ObjectDetectionConfig\x12)\n\x0b\x63lass_items\x18\x01 \x03(\x0b\x32\x14.rv.protos.ClassItem\x12\x11\n\tchip_size\x18\x02 \x02(\x05\x12M\n\x0c\x63hip_options\x18\x03 \x02(\x0b\x32\x37.rv.protos.TaskConfig.ObjectDetectionConfig.ChipOptions\x12S\n\x0fpredict_options\x18\x04 \x02(\x0b\x32:.rv.protos.TaskConfig.ObjectDetectionConfig.PredictOptions\x1ao\n\x0b\x43hipOptions\x12\x11\n\tneg_ratio\x18\x01 \x02(\x02\x12\x17\n\nioa_thresh\x18\x02 \x01(\x02:\x03\x30.8\x12\x1b\n\rwindow_method\x18\x03 \x01(\t:\x04\x63hip\x12\x17\n\x0clabel_buffer\x18\x04 \x01(\x02:\x01\x30\x1a\x46\n\x0ePredictOptions\x12\x19\n\x0cmerge_thresh\x18\x02 \x01(\x02:\x03\x30.5\x12\x19\n\x0cscore_thresh\x18\x03 \x01(\x02:\x03\x30.5\x1aX\n\x18\x43hipClassificationConfig\x12)\n\x0b\x63lass_items\x18\x01 \x03(\x0b\x32\x14.rv.protos.ClassItem\x12\x11\n\tchip_size\x18\x02 \x02(\x05\x1a\xa1\x03\n\x1aSemanticSegmentationConfig\x12)\n\x0b\x63lass_items\x18\x01 \x03(\x0b\x32\x14.rv.protos.ClassItem\x12\x11\n\tchip_size\x18\x02 \x02(\x05\x12R\n\x0c\x63hip_options\x18\x03 \x02(\x0b\x32<.rv.protos.TaskConfig.SemanticSegmentationConfig.ChipOptions\x1a\xf0\x01\n\x0b\x43hipOptions\x12$\n\rwindow_method\x18\x01 \x01(\t:\rrandom_sample\x12\x16\n\x0etarget_classes\x18\x02 \x03(\x05\x12$\n\x16\x64\x65\x62ug_chip_probability\x18\x03 \x01(\x02:\x04\x30.25\x12(\n\x1dnegative_survival_probability\x18\x04 \x01(\x02:\x01\x31\x12\x1d\n\x0f\x63hips_per_scene\x18\x05 \x01(\x05:\x04\x31\x30\x30\x30\x12$\n\x16target_count_threshold\x18\x06 \x01(\x05:\x04\x32\x30\x34\x38\x12\x0e\n\x06stride\x18\x07 \x01(\x05\x42\r\n\x0b\x63onfig_type')
  ,
  dependencies=[rastervision_dot_protos_dot_class__item__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TASKCONFIG_OBJECTDETECTIONCONFIG_CHIPOPTIONS = _descriptor.Descriptor(
  name='ChipOptions',
  full_name='rv.protos.TaskConfig.ObjectDetectionConfig.ChipOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='neg_ratio', full_name='rv.protos.TaskConfig.ObjectDetectionConfig.ChipOptions.neg_ratio', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ioa_thresh', full_name='rv.protos.TaskConfig.ObjectDetectionConfig.ChipOptions.ioa_thresh', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.8),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='window_method', full_name='rv.protos.TaskConfig.ObjectDetectionConfig.ChipOptions.window_method', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("chip").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_buffer', full_name='rv.protos.TaskConfig.ObjectDetectionConfig.ChipOptions.label_buffer', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
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
  serialized_start=814,
  serialized_end=925,
)

_TASKCONFIG_OBJECTDETECTIONCONFIG_PREDICTOPTIONS = _descriptor.Descriptor(
  name='PredictOptions',
  full_name='rv.protos.TaskConfig.ObjectDetectionConfig.PredictOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='merge_thresh', full_name='rv.protos.TaskConfig.ObjectDetectionConfig.PredictOptions.merge_thresh', index=0,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score_thresh', full_name='rv.protos.TaskConfig.ObjectDetectionConfig.PredictOptions.score_thresh', index=1,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
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
  serialized_start=927,
  serialized_end=997,
)

_TASKCONFIG_OBJECTDETECTIONCONFIG = _descriptor.Descriptor(
  name='ObjectDetectionConfig',
  full_name='rv.protos.TaskConfig.ObjectDetectionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_items', full_name='rv.protos.TaskConfig.ObjectDetectionConfig.class_items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_size', full_name='rv.protos.TaskConfig.ObjectDetectionConfig.chip_size', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_options', full_name='rv.protos.TaskConfig.ObjectDetectionConfig.chip_options', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predict_options', full_name='rv.protos.TaskConfig.ObjectDetectionConfig.predict_options', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TASKCONFIG_OBJECTDETECTIONCONFIG_CHIPOPTIONS, _TASKCONFIG_OBJECTDETECTIONCONFIG_PREDICTOPTIONS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=563,
  serialized_end=997,
)

_TASKCONFIG_CHIPCLASSIFICATIONCONFIG = _descriptor.Descriptor(
  name='ChipClassificationConfig',
  full_name='rv.protos.TaskConfig.ChipClassificationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_items', full_name='rv.protos.TaskConfig.ChipClassificationConfig.class_items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_size', full_name='rv.protos.TaskConfig.ChipClassificationConfig.chip_size', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=999,
  serialized_end=1087,
)

_TASKCONFIG_SEMANTICSEGMENTATIONCONFIG_CHIPOPTIONS = _descriptor.Descriptor(
  name='ChipOptions',
  full_name='rv.protos.TaskConfig.SemanticSegmentationConfig.ChipOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='window_method', full_name='rv.protos.TaskConfig.SemanticSegmentationConfig.ChipOptions.window_method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("random_sample").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_classes', full_name='rv.protos.TaskConfig.SemanticSegmentationConfig.ChipOptions.target_classes', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debug_chip_probability', full_name='rv.protos.TaskConfig.SemanticSegmentationConfig.ChipOptions.debug_chip_probability', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.25),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='negative_survival_probability', full_name='rv.protos.TaskConfig.SemanticSegmentationConfig.ChipOptions.negative_survival_probability', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chips_per_scene', full_name='rv.protos.TaskConfig.SemanticSegmentationConfig.ChipOptions.chips_per_scene', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_count_threshold', full_name='rv.protos.TaskConfig.SemanticSegmentationConfig.ChipOptions.target_count_threshold', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2048,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stride', full_name='rv.protos.TaskConfig.SemanticSegmentationConfig.ChipOptions.stride', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=1267,
  serialized_end=1507,
)

_TASKCONFIG_SEMANTICSEGMENTATIONCONFIG = _descriptor.Descriptor(
  name='SemanticSegmentationConfig',
  full_name='rv.protos.TaskConfig.SemanticSegmentationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_items', full_name='rv.protos.TaskConfig.SemanticSegmentationConfig.class_items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_size', full_name='rv.protos.TaskConfig.SemanticSegmentationConfig.chip_size', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_options', full_name='rv.protos.TaskConfig.SemanticSegmentationConfig.chip_options', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TASKCONFIG_SEMANTICSEGMENTATIONCONFIG_CHIPOPTIONS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1090,
  serialized_end=1507,
)

_TASKCONFIG = _descriptor.Descriptor(
  name='TaskConfig',
  full_name='rv.protos.TaskConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_type', full_name='rv.protos.TaskConfig.task_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predict_batch_size', full_name='rv.protos.TaskConfig.predict_batch_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predict_package_uri', full_name='rv.protos.TaskConfig.predict_package_uri', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debug', full_name='rv.protos.TaskConfig.debug', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predict_debug_uri', full_name='rv.protos.TaskConfig.predict_debug_uri', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_detection_config', full_name='rv.protos.TaskConfig.object_detection_config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_classification_config', full_name='rv.protos.TaskConfig.chip_classification_config', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='semantic_segmentation_config', full_name='rv.protos.TaskConfig.semantic_segmentation_config', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='custom_config', full_name='rv.protos.TaskConfig.custom_config', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TASKCONFIG_OBJECTDETECTIONCONFIG, _TASKCONFIG_CHIPCLASSIFICATIONCONFIG, _TASKCONFIG_SEMANTICSEGMENTATIONCONFIG, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='config_type', full_name='rv.protos.TaskConfig.config_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=114,
  serialized_end=1522,
)

_TASKCONFIG_OBJECTDETECTIONCONFIG_CHIPOPTIONS.containing_type = _TASKCONFIG_OBJECTDETECTIONCONFIG
_TASKCONFIG_OBJECTDETECTIONCONFIG_PREDICTOPTIONS.containing_type = _TASKCONFIG_OBJECTDETECTIONCONFIG
_TASKCONFIG_OBJECTDETECTIONCONFIG.fields_by_name['class_items'].message_type = rastervision_dot_protos_dot_class__item__pb2._CLASSITEM
_TASKCONFIG_OBJECTDETECTIONCONFIG.fields_by_name['chip_options'].message_type = _TASKCONFIG_OBJECTDETECTIONCONFIG_CHIPOPTIONS
_TASKCONFIG_OBJECTDETECTIONCONFIG.fields_by_name['predict_options'].message_type = _TASKCONFIG_OBJECTDETECTIONCONFIG_PREDICTOPTIONS
_TASKCONFIG_OBJECTDETECTIONCONFIG.containing_type = _TASKCONFIG
_TASKCONFIG_CHIPCLASSIFICATIONCONFIG.fields_by_name['class_items'].message_type = rastervision_dot_protos_dot_class__item__pb2._CLASSITEM
_TASKCONFIG_CHIPCLASSIFICATIONCONFIG.containing_type = _TASKCONFIG
_TASKCONFIG_SEMANTICSEGMENTATIONCONFIG_CHIPOPTIONS.containing_type = _TASKCONFIG_SEMANTICSEGMENTATIONCONFIG
_TASKCONFIG_SEMANTICSEGMENTATIONCONFIG.fields_by_name['class_items'].message_type = rastervision_dot_protos_dot_class__item__pb2._CLASSITEM
_TASKCONFIG_SEMANTICSEGMENTATIONCONFIG.fields_by_name['chip_options'].message_type = _TASKCONFIG_SEMANTICSEGMENTATIONCONFIG_CHIPOPTIONS
_TASKCONFIG_SEMANTICSEGMENTATIONCONFIG.containing_type = _TASKCONFIG
_TASKCONFIG.fields_by_name['object_detection_config'].message_type = _TASKCONFIG_OBJECTDETECTIONCONFIG
_TASKCONFIG.fields_by_name['chip_classification_config'].message_type = _TASKCONFIG_CHIPCLASSIFICATIONCONFIG
_TASKCONFIG.fields_by_name['semantic_segmentation_config'].message_type = _TASKCONFIG_SEMANTICSEGMENTATIONCONFIG
_TASKCONFIG.fields_by_name['custom_config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TASKCONFIG.oneofs_by_name['config_type'].fields.append(
  _TASKCONFIG.fields_by_name['object_detection_config'])
_TASKCONFIG.fields_by_name['object_detection_config'].containing_oneof = _TASKCONFIG.oneofs_by_name['config_type']
_TASKCONFIG.oneofs_by_name['config_type'].fields.append(
  _TASKCONFIG.fields_by_name['chip_classification_config'])
_TASKCONFIG.fields_by_name['chip_classification_config'].containing_oneof = _TASKCONFIG.oneofs_by_name['config_type']
_TASKCONFIG.oneofs_by_name['config_type'].fields.append(
  _TASKCONFIG.fields_by_name['semantic_segmentation_config'])
_TASKCONFIG.fields_by_name['semantic_segmentation_config'].containing_oneof = _TASKCONFIG.oneofs_by_name['config_type']
_TASKCONFIG.oneofs_by_name['config_type'].fields.append(
  _TASKCONFIG.fields_by_name['custom_config'])
_TASKCONFIG.fields_by_name['custom_config'].containing_oneof = _TASKCONFIG.oneofs_by_name['config_type']
DESCRIPTOR.message_types_by_name['TaskConfig'] = _TASKCONFIG

TaskConfig = _reflection.GeneratedProtocolMessageType('TaskConfig', (_message.Message,), dict(

  ObjectDetectionConfig = _reflection.GeneratedProtocolMessageType('ObjectDetectionConfig', (_message.Message,), dict(

    ChipOptions = _reflection.GeneratedProtocolMessageType('ChipOptions', (_message.Message,), dict(
      DESCRIPTOR = _TASKCONFIG_OBJECTDETECTIONCONFIG_CHIPOPTIONS,
      __module__ = 'rastervision.protos.task_pb2'
      # @@protoc_insertion_point(class_scope:rv.protos.TaskConfig.ObjectDetectionConfig.ChipOptions)
      ))
    ,

    PredictOptions = _reflection.GeneratedProtocolMessageType('PredictOptions', (_message.Message,), dict(
      DESCRIPTOR = _TASKCONFIG_OBJECTDETECTIONCONFIG_PREDICTOPTIONS,
      __module__ = 'rastervision.protos.task_pb2'
      # @@protoc_insertion_point(class_scope:rv.protos.TaskConfig.ObjectDetectionConfig.PredictOptions)
      ))
    ,
    DESCRIPTOR = _TASKCONFIG_OBJECTDETECTIONCONFIG,
    __module__ = 'rastervision.protos.task_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.TaskConfig.ObjectDetectionConfig)
    ))
  ,

  ChipClassificationConfig = _reflection.GeneratedProtocolMessageType('ChipClassificationConfig', (_message.Message,), dict(
    DESCRIPTOR = _TASKCONFIG_CHIPCLASSIFICATIONCONFIG,
    __module__ = 'rastervision.protos.task_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.TaskConfig.ChipClassificationConfig)
    ))
  ,

  SemanticSegmentationConfig = _reflection.GeneratedProtocolMessageType('SemanticSegmentationConfig', (_message.Message,), dict(

    ChipOptions = _reflection.GeneratedProtocolMessageType('ChipOptions', (_message.Message,), dict(
      DESCRIPTOR = _TASKCONFIG_SEMANTICSEGMENTATIONCONFIG_CHIPOPTIONS,
      __module__ = 'rastervision.protos.task_pb2'
      # @@protoc_insertion_point(class_scope:rv.protos.TaskConfig.SemanticSegmentationConfig.ChipOptions)
      ))
    ,
    DESCRIPTOR = _TASKCONFIG_SEMANTICSEGMENTATIONCONFIG,
    __module__ = 'rastervision.protos.task_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.TaskConfig.SemanticSegmentationConfig)
    ))
  ,
  DESCRIPTOR = _TASKCONFIG,
  __module__ = 'rastervision.protos.task_pb2'
  # @@protoc_insertion_point(class_scope:rv.protos.TaskConfig)
  ))
_sym_db.RegisterMessage(TaskConfig)
_sym_db.RegisterMessage(TaskConfig.ObjectDetectionConfig)
_sym_db.RegisterMessage(TaskConfig.ObjectDetectionConfig.ChipOptions)
_sym_db.RegisterMessage(TaskConfig.ObjectDetectionConfig.PredictOptions)
_sym_db.RegisterMessage(TaskConfig.ChipClassificationConfig)
_sym_db.RegisterMessage(TaskConfig.SemanticSegmentationConfig)
_sym_db.RegisterMessage(TaskConfig.SemanticSegmentationConfig.ChipOptions)


# @@protoc_insertion_point(module_scope)