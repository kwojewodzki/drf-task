from django.contrib.auth import get_user_model
from .models import User, ThumbnailSize, UserTier
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class ThumbnailSizeTest(TestCase):
    def test_create_thumbnail_size(self):
        thumbnail_size = ThumbnailSize.objects.create(size=200)
        self.assertEquals(thumbnail_size.size, 200)


class UserTierTest(TestCase):
    def setUp(self):
        self.user_tier = UserTier.objects.create(name='TestTier')
        self.user_tier.allowed_thumbnail_size.create(size=200)

    def test_create_user_tier(self):
        self.assertEquals(self.user_tier.name, 'TestTier')
        self.assertEquals(self.user_tier.allowed_thumbnail_size.first().size, 200)


class UserTest(TestCase):

    def test_create_basic_user(self):
        user = User.objects.create_user(username='username', password='Pas@w0rd', tier='BA')
        data = {
            'username': 'username',
            'password': 'Pas@w0rd',
            'tier': 'BA'
        }
        self.assertEquals(user.username, data['username'])
        self.assertEquals(user.tier, data['tier'])
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_premium_user(self):
        user = User.objects.create_user(username='username', password='Pas@w0rd', tier='PR')
        data = {
            'username': 'username',
            'password': 'Pas@w0rd',
            'tier': 'PR'
        }
        self.assertEquals(user.username, data['username'])
        self.assertEquals(user.tier, data['tier'])
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_enterprise_user(self):
        user = User.objects.create_user(username='username', password='Pas@w0rd', tier='EN')
        data = {
            'username': 'username',
            'password': 'Pas@w0rd',
            'tier': 'EN'
        }
        self.assertEquals(user.username, data['username'])
        self.assertEquals(user.tier, data['tier'])
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)


class LoginUserViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='username', password='Pas@w0rd')

    def test_login(self):
        data = {
            'username': 'username',
            'password': 'Pas@w0rd'
        }
        response = self.client.post('/login/', data)
        self.assertEquals(response.status_code, status.HTTP_202_ACCEPTED)
