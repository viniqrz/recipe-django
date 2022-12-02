from django.test import TestCase
from django.contrib.auth import get_user_model

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from core import models


def create_user(email='chico@example.com', password='password'):
    return get_user_model().objects.create_user(email, password)


TAG_URL = reverse('tag')


class TestTagApi(TestCase):

    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_create_recipe_succesful(self):
        payload = {
            'name': 'Chico'
        }

        res = self.client.post(payload)

        tag = models.Tag.objects.all().filter(user=self.user)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data, tag)
