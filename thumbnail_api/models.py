from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFill

from my_auth.models import User


def upload_to(instance, filename):
    return f'images/{filename}'.format(filename=filename)


class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image_200 = ImageSpecField(source='image_url', processors=[ResizeToFill(200, 200)], format='PNG',
                               options={'quality': 70})
    image_400 = ImageSpecField(source='image_url', processors=[ResizeToFill(400, 400)], format='PNG',
                               options={'quality': 70})
