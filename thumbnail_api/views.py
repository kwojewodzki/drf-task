from rest_framework import generics, parsers

from thumbnail_api.models import Image
from thumbnail_api.serializers import ImageSerializer


# Create your views here.

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
