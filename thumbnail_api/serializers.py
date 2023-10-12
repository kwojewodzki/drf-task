from rest_framework import serializers

from thumbnail_api.models import Image, ExpiringLink


class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'image_url'
        ]


class ImageListSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = [
            'images'
        ]

    def get_images(self, obj):
        request = self.context.get('request')
        return obj.get_links(request)


class ExpiringLinkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiringLink
        fields = [
            'image',
            'time_to_expire'
        ]
