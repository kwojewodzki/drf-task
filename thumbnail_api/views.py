from rest_framework import generics, parsers

from thumbnail_api.models import Image
from thumbnail_api.serializers import ImageSerializer, GetThumbnail200Serializer, GetThumbnail400Serializer, \
    GetOriginalImage


class ListImagesView(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(owner=user)


class UploadImageView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GetThumbnail200View(generics.RetrieveAPIView):
    serializer_class = GetThumbnail200Serializer
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(owner=user)


class GetThumbnail400View(generics.RetrieveAPIView):
    serializer_class = GetThumbnail400Serializer
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(owner=user)


class GetOriginalImageView(generics.RetrieveAPIView):
    serializer_class = GetOriginalImage
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(owner=user)
