"""Testing views."""

from rest_framework import status
from django.urls import reverse
from django.test import override_settings
from rest_framework.test import APITestCase
from API.models import Chat, Group
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken


class ChatListAPIViewTestCase(APITestCase):
    """Test for ChatListAPIView."""

    def setUp(self):
        """Set Up Method."""
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    @override_settings(
        CELERY_TASK_ALWAYS_EAGER=True,
        CELERY_BROKER_URL="memory://localhost/",
        CELERY_ACCEPT_CONTENT=["json"],
    )
    def test_chat_list_view(self):
        """Test the Chat list view."""
        Chat.objects.create(user=self.user, name="Chat 1", messages="Hello from chat 1")
        Chat.objects.create(user=self.user, name="Chat 2", messages="Hello from chat 2")
        chat_list_url = reverse("chat_list_api")
        response = self.client.get(chat_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(len(data["results"]), 2)
        self.assertEqual(data["results"][0]["name"], "Chat 1")
        self.assertEqual(data["results"][0]["messages"], "Hello from chat 1")
        self.assertEqual(data["results"][1]["name"], "Chat 2")
        self.assertEqual(data["results"][1]["messages"], "Hello from chat 2")

    @override_settings(
        CELERY_TASK_ALWAYS_EAGER=True,
        CELERY_BROKER_URL="memory://localhost/",
        CELERY_ACCEPT_CONTENT=["json"],
    )
    def test_chat_detail_view(self):
        """Test the Chat detail view."""
        chat = Chat.objects.create(
            user=self.user, name="Chat 1", messages="Hello from chat 1"
        )
        chat_detail_url = reverse("chat_detail_api", kwargs={"pk": chat.pk})
        response = self.client.get(chat_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data["name"], "Chat 1")
        self.assertEqual(data["messages"], "Hello from chat 1")

    @override_settings(
        CELERY_TASK_ALWAYS_EAGER=True,
        CELERY_BROKER_URL="memory://localhost/",
        CELERY_ACCEPT_CONTENT=["json"],
    )
    def test_group_list_view(self):
        """Test the Group list view."""
        group_data = {
            "title": "Group 1",
            "password": "test group",
            "description": "Test group 1",
        }
        response = self.client.post(reverse("group_list"), group_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(reverse("group_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(len(data["results"]), 1)
        self.assertEqual(data["results"][0]["title"], "Group 1")
        self.assertEqual(data["results"][0]["description"], "Test group 1")

    @override_settings(
        CELERY_TASK_ALWAYS_EAGER=True,
        CELERY_BROKER_URL="memory://localhost/",
        CELERY_ACCEPT_CONTENT=["json"],
    )
    def test_group_detail_view(self):
        """Test the Group detail view."""
        group = Group.objects.create(title="Group 1", description="Test group 1")
        group_detail_url = reverse("group_detail", kwargs={"pk": group.pk})

        # Test GET request to retrieve the group
        response = self.client.get(group_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data["title"], "Group 1")
        self.assertEqual(data["description"], "Test group 1")

        # Test PUT request to update the group
        updated_data = {"title": "Updated Group", "description": "Updated test group"}
        response = self.client.put(group_detail_url, updated_data, format="json")

        if response.status_code != status.HTTP_200_OK:
            print(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        group.refresh_from_db()
        self.assertEqual(group.title, "Updated Group")
        self.assertEqual(group.description, "Updated test group")

        # Test DELETE request to delete the group
        response = self.client.delete(group_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Group.objects.filter(pk=group.pk).exists())
