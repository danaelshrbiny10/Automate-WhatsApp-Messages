"""Core app models."""


from django.db import models


class TimeStampedModel(models.Model):
    """Abstract model provides created at and updated at fields."""

    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at ", auto_now_add=True)

    class Meta:
        """Meta class."""

        abstract = True
