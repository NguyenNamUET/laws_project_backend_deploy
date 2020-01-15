from rest_framework import serializers
from .models import ExtractiveDocument


class ExtractiveDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractiveDocument
        fields = '__all__'