from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from rest_framework import status

from my_auth.models import CustomUser, UserTier
from thumbnail_api.models import Image
from django.urls import reverse


# Create your tests here.

class TestImageModel(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='username', password='Pas@w0rd')
        self.image = Image.objects.create(
            owner=self.user,
            image_url='../test_image/test_image.jpg'
        )

    def test_image_owner(self):
        self.assertEquals(self.image.owner, self.user)


class ImageApiTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='username', password='Pas@w0rd',
                                                   tier=UserTier.objects.get(name='Enterprise'))
        self.image_file = SimpleUploadedFile(name='test_image.jpg',
                                             content=open("test_image/test_image.jpg", 'rb').read(),
                                             content_type='image/jpeg')
        self.image = Image.objects.create(
            owner=self.user,
            image_url='../test_image/test_image.jpg'
        )

    @override_settings(MEDIA_ROOT=('test_data' + '/media'))
    def test_upload_image(self):
        self.client.login(username='username', password='Pas@w0rd')
        url = reverse('upload_image')
        data = {'image_url': self.image_file}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Image.objects.count(), 2)

    def test_image_list_for_logged_out_user(self):
        self.client.logout()
        url = reverse('list_images')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_expiring_link_with_unauthorized_user(self):
        basic_tier = UserTier.objects.get(name='Basic')
        user = get_user_model().objects.create_user(
            username='testuser2',
            email='testuser2@email.com',
            password='testpass123',
            tier=basic_tier
        )
        self.client.login(username='testuser2', password='testpass123')
        url = reverse('generate_link')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
