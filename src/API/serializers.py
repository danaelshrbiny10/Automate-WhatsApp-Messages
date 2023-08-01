"""API App serializers."""

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from API.models import Chat, Group, Feedback


class ChatSerializer(serializers.ModelSerializer):
    """Chat Serializer class for chat model."""

    class Meta:
        model = Chat
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for the Group model."""

    # field1 = serializers.CharField(label=_("Field 1"))

    class Meta:
        model = Group
        fields = [
            "id",
            "title",
            "description",
            "members",
            "image",
            "admin",
            "slug",
            "password",
            "private",
            "invite_only",
            "allow_anonymous",
        ]
        read_only_fields = ["id", "slug"]
        extra_kwargs = {"password": {"write_only": True, "required": False}}

    def create(self, validated_data):
        """Handle ManyToManyField 'members' during creation."""
        members_data = validated_data.pop("members", [])
        group = super().create(validated_data)
        group.members.set(members_data)
        return group

    def update(self, instance, validated_data):
        """Handle ManyToManyField 'members' during update."""
        members_data = validated_data.pop("members", None)
        group = super().update(instance, validated_data)
        if members_data is not None:
            group.members.set(members_data)
        return group


class FeedbackSerializer(serializers.ModelSerializer):
    """Serializer for the Feedback model."""
    class Meta:
        model = Feedback
        fields = "__all__"
