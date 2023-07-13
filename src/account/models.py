"""Auth App models."""

from django.contrib.auth.models import User
from django.db import models
from core.models import TimeStampedModel


class Person(TimeStampedModel):
    """Person model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, verbose_name="Phone Number")

    def __str__(self) -> str:
        """Override str method."""
        return str(self.user)

    class Meta:
        """Meta class."""

        verbose_name = "Person"
        verbose_name_plural = "Persons"
