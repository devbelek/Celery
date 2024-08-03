from django.shortcuts import render
from .models import Image, Checks
from rest_framework import viewsets
from .serializers import ImageSerializer, CheckSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class CheckViewSet(viewsets.ModelViewSet):
    queryset = Checks.objects.all()
    serializer_class = CheckSerializer
