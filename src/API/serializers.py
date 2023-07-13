"""API App serializers."""

from rest_framework import serializers
from API.models import Chat, Group


class ChatSerializer(serializers.ModelSerializer):
    """Chat Serializer class for chat model."""

    class Meta:
        model = Chat
        fields = "__all__"
