from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ImageViewSet, CheckViewSet
from rest_framework import routers

router = DefaultRouter()
router.register(r'img', ImageViewSet)
router.register(r'checks', CheckViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

