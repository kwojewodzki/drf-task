from django.contrib.auth.models import AbstractUser
from django.db import models


class ThumbnailSize(models.Model):
    size = models.IntegerField()

    def __str__(self):
        return f'{self.size}px'


class UserTier(models.Model):
    name = models.CharField(max_length=32)
    allowed_thumbnail_size = models.ManyToManyField(ThumbnailSize)

    def __str__(self):
        return self.name


class User(AbstractUser):
    tier = models.ForeignKey(UserTier, on_delete=models.CASCADE, null=True)
