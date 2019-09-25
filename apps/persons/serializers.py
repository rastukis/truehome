# RestFramework
from rest_framework import serializers

from django_enum_choices.serializers import EnumChoiceField

# Enum
from enum import Enum


class VISBLE_TO_ENUM(Enum):
    PRIVATE = 1
    SHARED = 3


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=125, required=True, allow_blank=False, allow_null=False)
    owner_id = serializers.IntegerField(required=False, allow_null=True)
    org_id = serializers.IntegerField(required=False, allow_null=True)
    email = serializers.StringRelatedField(many=True, required=False, allow_null=True, allow_empty=True)
    phone = serializers.StringRelatedField(many=True, required=False, allow_null=True, allow_empty=True)
    visible_to = EnumChoiceField(VISBLE_TO_ENUM, required=False, allow_null=True)
    add_time = serializers.CharField(max_length=20, required=False, allow_null=True, allow_blank=True)


class PersonUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=125, required=False, allow_blank=True, allow_null=True)
    owner_id = serializers.IntegerField(required=False, allow_null=True)
    org_id = serializers.IntegerField(required=False, allow_null=True)
    email = serializers.StringRelatedField(many=True, required=False, allow_null=True, allow_empty=True)
    phone = serializers.StringRelatedField(many=True, required=False, allow_null=True, allow_empty=True)
    visible_to = EnumChoiceField(VISBLE_TO_ENUM, required=False, allow_null=True)
