import mimetypes
from django.http import FileResponse
from rest_framework import generics
from rest_framework.exceptions import NotFound, PermissionDenied

from my_auth.permissions import CanGetExpiringLink
from thumbnail_api.mixins import ExpiringLinkMixin
from thumbnail_api.models import Image, ExpiringLink
from thumbnail_api.serializers import ImageListSerializer, ImageCreateSerializer, ExpiringLinkCreateSerializer
from thumbnail_api.utils import convert_to_thumbnails


class ListImagesView(generics.ListAPIView):
    serializer_class = ImageListSerializer

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(owner=user)


class UploadImageView(generics.CreateAPIView):
    serializer_class = ImageCreateSerializer

    def perform_create(self, serializer):
        obj = serializer.save(owner=self.request.user)
        convert_to_thumbnails(obj.id)


class CreateExpiringLinkAPIView(generics.CreateAPIView, ExpiringLinkMixin):
    serializer_class = ExpiringLinkCreateSerializer
    permission_classes = [CanGetExpiringLink]

    def get_queryset(self):
        return ExpiringLink.objects.filter(image__owner=self.request.user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = self.link
        return response

    def perform_create(self, serializer):
        time_to_expire = self.request.data.get('time_to_expire')
        self.link = self.generate_expiring_link(serializer.validated_data['image'], time_to_expire)


class ExpiringLinkDetailAPIView(generics.RetrieveAPIView, ExpiringLinkMixin):
    queryset = ExpiringLink.objects.all()
    permission_classes = [CanGetExpiringLink]

    def get_object(self):
        signed_link = self.kwargs.get('signed_link')

        expiring_link_id = self.decode_signed_value(signed_link)
        expiring_link = generics.get_object_or_404(self.queryset, pk=expiring_link_id)
        if expiring_link.is_expired():
            expiring_link.delete()
            raise NotFound("Link has expired")

        if expiring_link.image.owner != self.request.user:
            raise PermissionDenied("User not authorized to view expiring link")

        return expiring_link.image

    def retrieve(self, request, *args, **kwargs):
        image = self.get_object().image_url
        content_type, encoding = mimetypes.guess_type(image.name)
        response = FileResponse(image, content_type=content_type, as_attachment=False,
                                filename=image.name.split('/')[-1])
        return response
