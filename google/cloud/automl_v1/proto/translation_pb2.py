# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1/proto/translation.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.automl_v1.proto import (
    data_items_pb2 as google_dot_cloud_dot_automl__v1_dot_proto_dot_data__items__pb2,
)
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1/proto/translation.proto",
    package="google.cloud.automl.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\032com.google.cloud.automl.v1B\020TranslationProtoP\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoMl\\V1\352\002\031Google::Cloud::AutoML::V1"
    ),
    serialized_pb=_b(
        '\n.google/cloud/automl_v1/proto/translation.proto\x12\x16google.cloud.automl.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a-google/cloud/automl_v1/proto/data_items.proto\x1a\x1cgoogle/api/annotations.proto"b\n\x1aTranslationDatasetMetadata\x12!\n\x14source_language_code\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12!\n\x14target_language_code\x18\x02 \x01(\tB\x03\xe0\x41\x02"K\n\x1cTranslationEvaluationMetrics\x12\x12\n\nbleu_score\x18\x01 \x01(\x01\x12\x17\n\x0f\x62\x61se_bleu_score\x18\x02 \x01(\x01"j\n\x18TranslationModelMetadata\x12\x12\n\nbase_model\x18\x01 \x01(\t\x12\x1c\n\x14source_language_code\x18\x02 \x01(\t\x12\x1c\n\x14target_language_code\x18\x03 \x01(\t"X\n\x15TranslationAnnotation\x12?\n\x12translated_content\x18\x01 \x01(\x0b\x32#.google.cloud.automl.v1.TextSnippetB\xbc\x01\n\x1a\x63om.google.cloud.automl.v1B\x10TranslationProtoP\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1_dot_proto_dot_data__items__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_TRANSLATIONDATASETMETADATA = _descriptor.Descriptor(
    name="TranslationDatasetMetadata",
    full_name="google.cloud.automl.v1.TranslationDatasetMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="source_language_code",
            full_name="google.cloud.automl.v1.TranslationDatasetMetadata.source_language_code",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="target_language_code",
            full_name="google.cloud.automl.v1.TranslationDatasetMetadata.target_language_code",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=184,
    serialized_end=282,
)


_TRANSLATIONEVALUATIONMETRICS = _descriptor.Descriptor(
    name="TranslationEvaluationMetrics",
    full_name="google.cloud.automl.v1.TranslationEvaluationMetrics",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="bleu_score",
            full_name="google.cloud.automl.v1.TranslationEvaluationMetrics.bleu_score",
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="base_bleu_score",
            full_name="google.cloud.automl.v1.TranslationEvaluationMetrics.base_bleu_score",
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=284,
    serialized_end=359,
)


_TRANSLATIONMODELMETADATA = _descriptor.Descriptor(
    name="TranslationModelMetadata",
    full_name="google.cloud.automl.v1.TranslationModelMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="base_model",
            full_name="google.cloud.automl.v1.TranslationModelMetadata.base_model",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="source_language_code",
            full_name="google.cloud.automl.v1.TranslationModelMetadata.source_language_code",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="target_language_code",
            full_name="google.cloud.automl.v1.TranslationModelMetadata.target_language_code",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=361,
    serialized_end=467,
)


_TRANSLATIONANNOTATION = _descriptor.Descriptor(
    name="TranslationAnnotation",
    full_name="google.cloud.automl.v1.TranslationAnnotation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="translated_content",
            full_name="google.cloud.automl.v1.TranslationAnnotation.translated_content",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=469,
    serialized_end=557,
)

_TRANSLATIONANNOTATION.fields_by_name[
    "translated_content"
].message_type = (
    google_dot_cloud_dot_automl__v1_dot_proto_dot_data__items__pb2._TEXTSNIPPET
)
DESCRIPTOR.message_types_by_name[
    "TranslationDatasetMetadata"
] = _TRANSLATIONDATASETMETADATA
DESCRIPTOR.message_types_by_name[
    "TranslationEvaluationMetrics"
] = _TRANSLATIONEVALUATIONMETRICS
DESCRIPTOR.message_types_by_name["TranslationModelMetadata"] = _TRANSLATIONMODELMETADATA
DESCRIPTOR.message_types_by_name["TranslationAnnotation"] = _TRANSLATIONANNOTATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TranslationDatasetMetadata = _reflection.GeneratedProtocolMessageType(
    "TranslationDatasetMetadata",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TRANSLATIONDATASETMETADATA,
        __module__="google.cloud.automl_v1.proto.translation_pb2",
        __doc__="""Dataset metadata that is specific to translation.
  
  
  Attributes:
      source_language_code:
          Required. The BCP-47 language code of the source language.
      target_language_code:
          Required. The BCP-47 language code of the target language.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.TranslationDatasetMetadata)
    ),
)
_sym_db.RegisterMessage(TranslationDatasetMetadata)

TranslationEvaluationMetrics = _reflection.GeneratedProtocolMessageType(
    "TranslationEvaluationMetrics",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TRANSLATIONEVALUATIONMETRICS,
        __module__="google.cloud.automl_v1.proto.translation_pb2",
        __doc__="""Evaluation metrics for the dataset.
  
  
  Attributes:
      bleu_score:
          Output only. BLEU score.
      base_bleu_score:
          Output only. BLEU score for base model.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.TranslationEvaluationMetrics)
    ),
)
_sym_db.RegisterMessage(TranslationEvaluationMetrics)

TranslationModelMetadata = _reflection.GeneratedProtocolMessageType(
    "TranslationModelMetadata",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TRANSLATIONMODELMETADATA,
        __module__="google.cloud.automl_v1.proto.translation_pb2",
        __doc__="""Model metadata that is specific to translation.
  
  
  Attributes:
      base_model:
          The resource name of the model to use as a baseline to train
          the custom model. If unset, we use the default base model
          provided by Google Translate. Format: ``projects/{project_id}/
          locations/{location_id}/models/{model_id}``
      source_language_code:
          Output only. Inferred from the dataset. The source language
          (The BCP-47 language code) that is used for training.
      target_language_code:
          Output only. The target language (The BCP-47 language code)
          that is used for training.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.TranslationModelMetadata)
    ),
)
_sym_db.RegisterMessage(TranslationModelMetadata)

TranslationAnnotation = _reflection.GeneratedProtocolMessageType(
    "TranslationAnnotation",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TRANSLATIONANNOTATION,
        __module__="google.cloud.automl_v1.proto.translation_pb2",
        __doc__="""Annotation details specific to translation.
  
  
  Attributes:
      translated_content:
          Output only . The translated content.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.TranslationAnnotation)
    ),
)
_sym_db.RegisterMessage(TranslationAnnotation)


DESCRIPTOR._options = None
_TRANSLATIONDATASETMETADATA.fields_by_name["source_language_code"]._options = None
_TRANSLATIONDATASETMETADATA.fields_by_name["target_language_code"]._options = None
# @@protoc_insertion_point(module_scope)
