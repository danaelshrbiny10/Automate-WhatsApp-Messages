"""Auth App serializers."""

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from account.models import Person
import re


class PersonSerializer(serializers.Serializer):
    """Person serializer class for person model."""

    username = serializers.CharField(
        max_length=10, required=True, validators=[UniqueValidator(User.objects.all())]
    )

    password = serializers.CharField(required=True)

    def validate_password(self, value: str) -> str:
        """Validate the length of a new password"""
        if len(value) < 8:
            raise serializers.ValidationError("Password is short.")
        return value

    def create(self, validated_data: dict) -> Person:
        """Create Person."""
        return self._create_profile(validated_data=validated_data)

    def _create_user(self, validated_data: dict) -> User:
        """Private method to create user object."""
        return User.objects.create_user(
            username=validated_data.get("username"),
            password=validated_data.get("password"),
        )

    def _create_profile(self, validated_data: dict) -> Person:
        """Private method to create user profile object."""
        return Person.objects.create(
            user=self._create_user(validated_data=validated_data),
        )
