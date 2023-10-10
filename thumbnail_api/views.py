import mimetypes
from django.http import FileResponse
from rest_framework import generics
from rest_framework.exceptions import NotFound, PermissionDenied

from my_auth.permissions import CanGetExpiringLink
from thumbnail_api.mixins import ExpiringLinkMixin
from thumbnail_api.models import Image, ExpiringLink
from thumbnail_api.serializers import ImageListSerializer, ImageCreateSerializer
from thumbnail_api.utils import convert_to_thumbnails


class ListImagesView(generics.ListAPIView):
    serializer_class = ImageListSerializer

    def get_queryset(self):
        user = self.request.user
        print(user.tier.get_thumbnail_size())
        return Image.objects.filter(owner=user)


class UploadImageView(generics.CreateAPIView):
    serializer_class = ImageCreateSerializer

    def perform_create(self, serializer):
        obj = serializer.save(owner=self.request.user)
        print(obj.id)
        convert_to_thumbnails(obj.id)

