from unittest import TestCase

from django.urls import reverse, resolve
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.utils import json

from rest_framework.views import APIView
# self.client = APIClient()
from docker.settings import SIMPLE_JWT
from docker_admin.views import WomenAPIList


class ApiUrlsTests(TestCase):

    def test_get_customers_is_resolved(self):
        url = reverse('margo')
        self.assertEquals(resolve(url).func.view_class, WomenAPIList)


class CustomerAPIViewTests(APITestCase):  # new here
    url = reverse("margo")

    def setUp(self):
        self.user = User.objects.create_user(
            username='zlava', password='1902')
        self.token = Token.objects.create(user=self.user)
        # self.client = Client()
        # self.client.login(email=self.user.email, password=self.pa
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_customers_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_customers_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 401)

    def test_post_customer_authenticated(self):
        data = {
            "id": 1,
            'title': 'LOGIN',
            'content': 'COOL PUT GET DELETE',
            # "time_create": "2022-11-17T22:38:11.840967Z",
            'is_published': True,
            'cat_id': 'программирование',

        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class RouterTestApi(APITestCase):
    url = reverse('margo')

    def setUp(self):
        self.user = User.objects.create_user(
            username='zlava', password='1902')
        self.token = Token.objects.create(user=self.user)
        # self.client = Client()
        # self.client.login(email=self.user.email, password=self.pa
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        data = {
            "id": 1,
            'title': 'LOGIN',
            'content': 'COOL PUT GET DELETE',
            # "time_create": "2022-11-17T22:38:11.840967Z",
            'is_published': True,
            'cat_id': 'программирование',

        }
        self.client.post(self.url, data, format='json')

    def test_router_simple_costumer(self):
        # costumer_url = reverse('main', args=[1])
        response = self.client.get("/api/3/")
        self.assertEqual(response.data['title'], 'LOGIN')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['title'], 'LOGIN')

    def test_get_customers_un_authenticated(self):
        # costumer_url = reverse('main', args=[1])
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(reverse("main", args=[1]))
        self.assertEquals(response.status_code, 401)
