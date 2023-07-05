"""Whatsapp API App admin."""

from django.contrib import admin
from .models import Chat, Group


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    """Admin class for Chat model."""

    list_display = (
        "user",
        "name",
        "is_groupchat",
        "messages",
        "phone_number",
        "last_messaged_time",
        "unread_messages_count",
    )
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = (
        (
            "Chat Information",
            {
                "fields": (
                    "user",
                    "name",
                    "is_groupchat",
                    "messages",
                    "phone_number",
                    "last_messaged_time",
                    "unread_messages_count",
                ),
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
            },
        ),
    )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Admin class for Group model."""

    list_display = (
        "title",
        "description",
        "image",
        "admin",
        "slug",
        "password",
        "private",
        "invite_only",
        "allow_anonymous",
    )
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = (
        (
            "Group Information",
            {
                "fields": (
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
                ),
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
            },
        ),
    )

    def has_add_permission(self, request):
        """Returns False to disable add permission."""
        return False

    def has_change_permission(self, request, obj=None):
        """Returns False to disable change permission."""
        return False

    def has_delete_permission(self, request, obj=None):
        """Returns False to disable delete permission."""
        return False
