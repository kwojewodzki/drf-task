from django.contrib.auth.models import AbstractUser
from django.db import models


class ThumbnailSize(models.Model):
    size = models.IntegerField()

    def __str__(self):
        return f'{self.size}px'


class UserTier(models.Model):
    name = models.CharField(max_length=32)
    allowed_thumbnail_size = models.ManyToManyField(ThumbnailSize)
    is_expiring_link = models.BooleanField(default=False)
    is_original_file = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_thumbnail_size(self):
        sizes = [x.size for x in self.allowed_thumbnail_size.all()]
        return sizes


class CustomUser(AbstractUser):
    tier = models.ForeignKey(UserTier, on_delete=models.CASCADE, null=True)
