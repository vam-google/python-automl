# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/model_evaluation.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.automl_v1beta1.proto import (
    classification_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    detection_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_detection__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    regression_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_regression__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    tables_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_tables__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    text_extraction_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__extraction__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    text_sentiment_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__sentiment__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    translation_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_translation__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/model_evaluation.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1"
    ),
    serialized_pb=_b(
        '\n8google/cloud/automl_v1beta1/proto/model_evaluation.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x19google/api/resource.proto\x1a\x36google/cloud/automl_v1beta1/proto/classification.proto\x1a\x31google/cloud/automl_v1beta1/proto/detection.proto\x1a\x32google/cloud/automl_v1beta1/proto/regression.proto\x1a.google/cloud/automl_v1beta1/proto/tables.proto\x1a\x37google/cloud/automl_v1beta1/proto/text_extraction.proto\x1a\x36google/cloud/automl_v1beta1/proto/text_sentiment.proto\x1a\x33google/cloud/automl_v1beta1/proto/translation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto"\xb1\x08\n\x0fModelEvaluation\x12i\n!classification_evaluation_metrics\x18\x08 \x01(\x0b\x32<.google.cloud.automl.v1beta1.ClassificationEvaluationMetricsH\x00\x12\x61\n\x1dregression_evaluation_metrics\x18\x18 \x01(\x0b\x32\x38.google.cloud.automl.v1beta1.RegressionEvaluationMetricsH\x00\x12\x63\n\x1etranslation_evaluation_metrics\x18\t \x01(\x0b\x32\x39.google.cloud.automl.v1beta1.TranslationEvaluationMetricsH\x00\x12w\n)image_object_detection_evaluation_metrics\x18\x0c \x01(\x0b\x32\x42.google.cloud.automl.v1beta1.ImageObjectDetectionEvaluationMetricsH\x00\x12u\n(video_object_tracking_evaluation_metrics\x18\x0e \x01(\x0b\x32\x41.google.cloud.automl.v1beta1.VideoObjectTrackingEvaluationMetricsH\x00\x12h\n!text_sentiment_evaluation_metrics\x18\x0b \x01(\x0b\x32;.google.cloud.automl.v1beta1.TextSentimentEvaluationMetricsH\x00\x12j\n"text_extraction_evaluation_metrics\x18\r \x01(\x0b\x32<.google.cloud.automl.v1beta1.TextExtractionEvaluationMetricsH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x12\x61nnotation_spec_id\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x0f \x01(\t\x12/\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1f\n\x17\x65valuated_example_count\x18\x06 \x01(\x05:\x87\x01\xea\x41\x83\x01\n%automl.googleapis.com/ModelEvaluation\x12Zprojects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}B\t\n\x07metricsB\xa5\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_detection__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_regression__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_tables__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__extraction__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__sentiment__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_translation__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_MODELEVALUATION = _descriptor.Descriptor(
    name="ModelEvaluation",
    full_name="google.cloud.automl.v1beta1.ModelEvaluation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="classification_evaluation_metrics",
            full_name="google.cloud.automl.v1beta1.ModelEvaluation.classification_evaluation_metrics",
            index=0,
            number=8,
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
        ),
        _descriptor.FieldDescriptor(
            name="regression_evaluation_metrics",
            full_name="google.cloud.automl.v1beta1.ModelEvaluation.regression_evaluation_metrics",
            index=1,
            number=24,
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
        ),
        _descriptor.FieldDescriptor(
            name="translation_evaluation_metrics",
            full_name="google.cloud.automl.v1beta1.ModelEvaluation.translation_evaluation_metrics",
            index=2,
            number=9,
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
        ),
        _descriptor.FieldDescriptor(
            name="image_object_detection_evaluation_metrics",
            full_name="google.cloud.automl.v1beta1.ModelEvaluation.image_object_detection_evaluation_metrics",
            index=3,
            number=12,
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
        ),
        _descriptor.FieldDescriptor(
            name="video_object_tracking_evaluation_metrics",
            full_name="google.cloud.automl.v1beta1.ModelEvaluation.video_object_tracking_evaluation_metrics",
            index=4,
            number=14,
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
        ),
        _descriptor.FieldDescriptor(
            name="text_sentiment_evaluation_metrics",
            full_name="google.cloud.automl.v1beta1.ModelEvaluation.text_sentiment_evaluation_metrics",
            index=5,
            number=11,
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
        ),
        _descriptor.FieldDescriptor(
            name="text_extraction_evaluation_metrics",
            full_name="google.cloud.automl.v1beta1.ModelEvaluation.text_extraction_evaluation_metrics",
            index=6,
            number=13,
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
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.automl.v1beta1.ModelEvaluation.name",
            index=7,
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
            name="annotation_spec_id",
            full_name="google.cloud.automl.v1beta1.ModelEvaluation.annotation_spec_id",
            index=8,
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
            name="display_name",
            full_name="google.cloud.automl.v1beta1.ModelEvaluation.display_name",
            index=9,
            number=15,
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
            name="create_time",
            full_name="google.cloud.automl.v1beta1.ModelEvaluation.create_time",
            index=10,
            number=5,
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
        ),
        _descriptor.FieldDescriptor(
            name="evaluated_example_count",
            full_name="google.cloud.automl.v1beta1.ModelEvaluation.evaluated_example_count",
            index=11,
            number=6,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
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
    serialized_options=_b(
        "\352A\203\001\n%automl.googleapis.com/ModelEvaluation\022Zprojects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}"
    ),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="metrics",
            full_name="google.cloud.automl.v1beta1.ModelEvaluation.metrics",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=553,
    serialized_end=1626,
)

_MODELEVALUATION.fields_by_name[
    "classification_evaluation_metrics"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2._CLASSIFICATIONEVALUATIONMETRICS
)
_MODELEVALUATION.fields_by_name[
    "regression_evaluation_metrics"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_regression__pb2._REGRESSIONEVALUATIONMETRICS
)
_MODELEVALUATION.fields_by_name[
    "translation_evaluation_metrics"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_translation__pb2._TRANSLATIONEVALUATIONMETRICS
)
_MODELEVALUATION.fields_by_name[
    "image_object_detection_evaluation_metrics"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_detection__pb2._IMAGEOBJECTDETECTIONEVALUATIONMETRICS
)
_MODELEVALUATION.fields_by_name[
    "video_object_tracking_evaluation_metrics"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_detection__pb2._VIDEOOBJECTTRACKINGEVALUATIONMETRICS
)
_MODELEVALUATION.fields_by_name[
    "text_sentiment_evaluation_metrics"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__sentiment__pb2._TEXTSENTIMENTEVALUATIONMETRICS
)
_MODELEVALUATION.fields_by_name[
    "text_extraction_evaluation_metrics"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__extraction__pb2._TEXTEXTRACTIONEVALUATIONMETRICS
)
_MODELEVALUATION.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MODELEVALUATION.oneofs_by_name["metrics"].fields.append(
    _MODELEVALUATION.fields_by_name["classification_evaluation_metrics"]
)
_MODELEVALUATION.fields_by_name[
    "classification_evaluation_metrics"
].containing_oneof = _MODELEVALUATION.oneofs_by_name["metrics"]
_MODELEVALUATION.oneofs_by_name["metrics"].fields.append(
    _MODELEVALUATION.fields_by_name["regression_evaluation_metrics"]
)
_MODELEVALUATION.fields_by_name[
    "regression_evaluation_metrics"
].containing_oneof = _MODELEVALUATION.oneofs_by_name["metrics"]
_MODELEVALUATION.oneofs_by_name["metrics"].fields.append(
    _MODELEVALUATION.fields_by_name["translation_evaluation_metrics"]
)
_MODELEVALUATION.fields_by_name[
    "translation_evaluation_metrics"
].containing_oneof = _MODELEVALUATION.oneofs_by_name["metrics"]
_MODELEVALUATION.oneofs_by_name["metrics"].fields.append(
    _MODELEVALUATION.fields_by_name["image_object_detection_evaluation_metrics"]
)
_MODELEVALUATION.fields_by_name[
    "image_object_detection_evaluation_metrics"
].containing_oneof = _MODELEVALUATION.oneofs_by_name["metrics"]
_MODELEVALUATION.oneofs_by_name["metrics"].fields.append(
    _MODELEVALUATION.fields_by_name["video_object_tracking_evaluation_metrics"]
)
_MODELEVALUATION.fields_by_name[
    "video_object_tracking_evaluation_metrics"
].containing_oneof = _MODELEVALUATION.oneofs_by_name["metrics"]
_MODELEVALUATION.oneofs_by_name["metrics"].fields.append(
    _MODELEVALUATION.fields_by_name["text_sentiment_evaluation_metrics"]
)
_MODELEVALUATION.fields_by_name[
    "text_sentiment_evaluation_metrics"
].containing_oneof = _MODELEVALUATION.oneofs_by_name["metrics"]
_MODELEVALUATION.oneofs_by_name["metrics"].fields.append(
    _MODELEVALUATION.fields_by_name["text_extraction_evaluation_metrics"]
)
_MODELEVALUATION.fields_by_name[
    "text_extraction_evaluation_metrics"
].containing_oneof = _MODELEVALUATION.oneofs_by_name["metrics"]
DESCRIPTOR.message_types_by_name["ModelEvaluation"] = _MODELEVALUATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelEvaluation = _reflection.GeneratedProtocolMessageType(
    "ModelEvaluation",
    (_message.Message,),
    dict(
        DESCRIPTOR=_MODELEVALUATION,
        __module__="google.cloud.automl_v1beta1.proto.model_evaluation_pb2",
        __doc__="""Evaluation results of a model.
  
  
  Attributes:
      metrics:
          Output only. Problem type specific evaluation metrics.
      classification_evaluation_metrics:
          Model evaluation metrics for image, text, video and tables
          classification. Tables problem is considered a classification
          when the target column is CATEGORY DataType.
      regression_evaluation_metrics:
          Model evaluation metrics for Tables regression. Tables problem
          is considered a regression when the target column has FLOAT64
          DataType.
      translation_evaluation_metrics:
          Model evaluation metrics for translation.
      image_object_detection_evaluation_metrics:
          Model evaluation metrics for image object detection.
      video_object_tracking_evaluation_metrics:
          Model evaluation metrics for video object tracking.
      text_sentiment_evaluation_metrics:
          Evaluation metrics for text sentiment models.
      text_extraction_evaluation_metrics:
          Evaluation metrics for text extraction models.
      name:
          Output only. Resource name of the model evaluation. Format:  `
          `projects/{project_id}/locations/{location_id}/models/{model_i
          d}/modelEvaluations/{model_evaluation_id}``
      annotation_spec_id:
          Output only. The ID of the annotation spec that the model
          evaluation applies to. The The ID is empty for the overall
          model evaluation. For Tables annotation specs in the dataset
          do not exist and this ID is always not set, but for
          CLASSIFICATION  [prediction\_type-s][google.cloud.automl.v1bet
          a1.TablesModelMetadata.prediction\_type] the [display\_name][g
          oogle.cloud.automl.v1beta1.ModelEvaluation.display\_name]
          field is used.
      display_name:
          Output only. The value of [display\_name][google.cloud.automl.
          v1beta1.AnnotationSpec.display\_name] at the moment when the
          model was trained. Because this field returns a value at model
          training time, for different models trained from the same
          dataset, the values may differ, since display names could had
          been changed between the two model's trainings. For Tables
          CLASSIFICATION  [prediction\_type-s][google.cloud.automl.v1bet
          a1.TablesModelMetadata.prediction\_type] distinct values of
          the target column at the moment of the model evaluation are
          populated here. The display\_name is empty for the overall
          model evaluation.
      create_time:
          Output only. Timestamp when this model evaluation was created.
      evaluated_example_count:
          Output only. The number of examples used for model evaluation,
          i.e. for which ground truth from time of model creation is
          compared against the predicted annotations created by the
          model. For overall ModelEvaluation (i.e. with
          annotation\_spec\_id not set) this is the total number of all
          examples used for evaluation. Otherwise, this is the count of
          examples that according to the ground truth were annotated by
          the  [annotation\_spec\_id][google.cloud.automl.v1beta1.ModelE
          valuation.annotation\_spec\_id].
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ModelEvaluation)
    ),
)
_sym_db.RegisterMessage(ModelEvaluation)


DESCRIPTOR._options = None
_MODELEVALUATION._options = None
# @@protoc_insertion_point(module_scope)
