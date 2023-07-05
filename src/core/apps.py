# coding=utf-8
"""Core App Apps."""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Class representing the Core app and its configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    verbose_name = "Core"
