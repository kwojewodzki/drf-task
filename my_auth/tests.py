from my_auth.models import CustomUser, ThumbnailSize, UserTier
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase


class ThumbnailSizeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.thumbnail = ThumbnailSize.objects.create(id=15, size=250)

    def test_create_thumbnail_size(self):
        self.assertEquals(self.thumbnail.size, 250)


class UserTierTest(TestCase):
    def setUp(self):
        self.user_tier = UserTier.objects.create(id=15, name='TestTier', is_original_file=True, is_expiring_link=False)
        self.user_tier.allowed_thumbnail_size.create(id=15, size=250)

    def test_create_user_tier(self):
        self.assertEquals(self.user_tier.name, 'TestTier')
        self.assertEquals(self.user_tier.allowed_thumbnail_size.first().size, 250)

    def test_is_expiring_link(self):
        self.assertFalse(self.user_tier.is_expiring_link)

    def test_is_original_file(self):
        self.assertTrue(self.user_tier.is_original_file)


class UserTest(TestCase):
    def setUp(self):
        self.user_tier = UserTier.objects.filter(name="Basic").get()
        self.user = CustomUser.objects.create_user(id=15, username='username', password='Pas@w0rd', tier=self.user_tier)

    def test_create_basic_user(self):
        data = {
            'username': 'username',
            'password': 'Pas@w0rd',
        }
        self.assertEquals(self.user.username, data['username'])
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)

    def test_is_expiring_link(self):
        self.assertFalse(self.user.tier.is_expiring_link)

    def test_is_original_link(self):
        self.assertFalse(self.user.tier.is_original_file)


class LoginUserViewTest(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='username', password='Pas@w0rd')

    def test_login(self):
        data = {
            'username': 'username',
            'password': 'Pas@w0rd'
        }
        response = self.client.post('/auth/login/', data)
        self.assertEquals(response.status_code, status.HTTP_202_ACCEPTED)
