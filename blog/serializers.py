from .models import Image, Checks
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checks
        fields = '__all__'