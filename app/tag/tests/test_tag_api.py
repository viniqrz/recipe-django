from django.test import TestCase
from django.contrib.auth import get_user_model

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from core import models


def create_user(email='chico@example.com', password='password'):
    return get_user_model().objects.create_user(email, password)


TAG_URL = reverse('tag:tag-list')


class TestTagApi(TestCase):

    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_create_tag_succesful(self):
        payload = {
            'name': 'Chico'
        }

        res = self.client.post(TAG_URL, payload)

        tag = models.Tag.objects.filter(user=self.user).first()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(tag.name, payload['name'])
        self.assertEqual(tag.user, self.user)
