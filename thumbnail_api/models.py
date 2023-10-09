from django.db import models

from my_auth.models import User


def upload_to(instance, filename):
    return f'images/{filename}'.format(filename=filename)


class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
