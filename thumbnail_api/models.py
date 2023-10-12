import time
from pathlib import Path

import uuid
from django.conf import settings
from django.core.files.storage import default_storage
from django.db import models
import os

from my_auth.models import CustomUser
from thumbnail_api.validators import validate_time_to_expire


def upload_to(instance, filename):
    return f"{instance.owner.id}/images/{instance.id}/{filename}"


class Image(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def get_filename(self):
        return Path(f'{self.image_url}').stem

    def get_links(self, request):
        user_tier = self.owner.tier
        base_file = os.path.dirname(self.image_url.name)
        thumbnails = default_storage.listdir(base_file)[1]
        base_url = request.build_absolute_uri('/')
        thumbs_for_user = []
        for thumbnail in thumbnails:
            if 'thumb' in thumbnail:
                thumbnails_path = os.path.join(base_file, thumbnail)
                thumbs_for_user.append(base_url + settings.MEDIA_URL + thumbnails_path)

        if user_tier.is_original_file:
            thumbs_for_user.append(base_url + self.image_url.url)

        if user_tier.is_expiring_link and hasattr(self, 'expiring_link'):
            thumbs_for_user.append(self.expiring_link.link)

        return thumbs_for_user


class ExpiringLink(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    image = models.OneToOneField(Image, on_delete=models.CASCADE)
    link = models.CharField(max_length=256)
    time_to_expire = models.IntegerField(validators=[validate_time_to_expire])

    def is_expired(self):
        current_time = time.time()
        return current_time > self.time_to_expire
