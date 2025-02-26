from rest_framework import serializers
from .models import ScannedDocument

class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScannedDocument
        fields = '__all__'