"""API App test."""

from django.test import TestCase
from django.urls import reverse
from API.models import Chat, Group
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken


class APITestUrls(TestCase):
    """Test for API URL."""

    def setUp(self):
        """Set Up Method."""
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.chat_list_api = reverse("chat_list_api")
        self.group_list = reverse("group_list")

    def test_chat_list_url(self):
        """Test the Chat list."""
        response = self.client.get(self.chat_list_api)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_chat_detail(self):
        """Test the Chat detail."""
        chat = Chat.objects.create(user=self.user, name="Test Chat", messages="Hello")
        chat_detail_url = reverse("chat_detail_api", args=[chat.pk])
        response = self.client.get(chat_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_group_list(self):
        """Test the Group list."""
        response = self.client.get(self.group_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_group_detail(self):
        """Test the Group detail."""
        group = Group.objects.create(title="Test Group", description="Hello")
        group_detail_url = reverse("group_detail", args=[group.pk])
        response = self.client.get(group_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_chat_detail(self):
        """Test for retrieving a chat with an invalid chat ID."""
        invalid_chat_id = 9999
        invalid_chat_detail_url = reverse("chat_detail_api", args=[invalid_chat_id])
        response = self.client.get(invalid_chat_detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_group_detail(self):
        """Test for retrieving a group with an invalid group ID."""
        invalid_group_id = 9999
        invalid_group_detail_url = reverse("group_detail", args=[invalid_group_id])
        response = self.client.get(invalid_group_detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
