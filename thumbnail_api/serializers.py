from imagekit.cachefiles import ImageCacheFile
from rest_framework import serializers
from .models import Image
from .utils import Thumbnail


class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Image
        fields = ['id', 'owner', 'image_url']


class GetThumbnail200Serializer(serializers.ModelSerializer):
    image_200 = serializers.ImageField()

    class Meta:
        model = Image
        fields = ['image_200']


class GetThumbnail400Serializer(serializers.ModelSerializer):
    image_400 = serializers.ImageField()

    class Meta:
        model = Image
        fields = ['image_400']


class GetOriginalImage(serializers.ModelSerializer):
    image_url = serializers.ImageField()

    class Meta:
        model = Image
        fields = ['image_url']
