from rest_framework import serializers

from client.models import ClientProfile
from .schemas.serializers import client_serializer_schema


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = '__all__'
        swagger_schema_fields = client_serializer_schema
