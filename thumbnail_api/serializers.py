from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Image
        fields = ['id', 'owner', 'image_url']
