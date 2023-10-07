from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


# Create your tests here.

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
