from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

class UserTests(APITestCase):
    """Tests for user authentication"""

    def setUp(self):
        self.client = APIClient()
        self.user_data = {"username": "testuser", "password": "testpass"}
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_register_user(self):
        """Ensure we can register a new user"""
        payload = {"username": "newuser", "password": "newpass"}
        response = self.client.post("/api/register/", payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(get_user_model().objects.filter(username="newuser").exists())

    def test_login_user(self):
        """Ensure we can login a user and get tokens"""
        response = self.client.post("/api/login/", self.user_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_protected_route_requires_auth(self):
        """Ensure protected routes require authentication"""
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authenticate and try again
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

