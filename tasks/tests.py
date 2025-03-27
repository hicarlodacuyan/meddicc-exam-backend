from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import Task

class TaskTests(APITestCase):
    """Tests for the task model and API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)  # Authenticate user

        # Create a test task
        self.task = Task.objects.create(name="Test Task", description="Task description", user=self.user)

    def test_create_task(self):
        """Ensure we can create a new task"""
        payload = {
            "name": "New Task",
            "description": "New task description"
        }
        response = self.client.post("/api/tasks/", payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], payload["name"])

    def test_get_task_list(self):
        """Ensure we can retrieve task list"""
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)  # At least one task exists

    def test_update_task(self):
        """Ensure we can update a task"""
        payload = {"name": "Updated Task Name"}
        response = self.client.patch(f"/api/tasks/{self.task.id}/", payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, payload["name"])

    def test_delete_task(self):
        """Ensure we can delete a task"""
        response = self.client.delete(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

