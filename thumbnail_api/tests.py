from django.test import TestCase

from my_auth.models import CustomUser
from thumbnail_api.models import Image


# Create your tests here.

class TestImageModel(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='username', password='Pas@w0rd')
        self.image = Image.objects.create(
            owner=self.user,
            image_url=''
        )