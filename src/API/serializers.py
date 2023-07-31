"""API App serializers."""

from rest_framework import serializers
from API.models import Chat, Group


class ChatSerializer(serializers.ModelSerializer):
    """Chat Serializer class for chat model."""

    class Meta:
        model = Chat
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for the Group model."""

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
        extra_kwargs = {"password": {"write_only": False, "required": False}}

    def create(self, validated_data):
        """Override create method to handle ManyToManyField 'members'."""
        members_data = validated_data.pop("members", [])
        group = Group.objects.create(**validated_data)
        group.members.set(members_data)
        return group

    def update(self, instance, validated_data):
        """Override update method to handle ManyToManyField 'members'."""
        members_data = validated_data.pop("members", None)
        group = super().update(instance, validated_data)
        if members_data is not None:
            group.members.set(members_data)
        return group
