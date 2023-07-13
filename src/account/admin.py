"""Auth App admin."""

from django.contrib import admin
from .models import Person

# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Admin class for Person model."""

    list_display = ("user")
    fieldsets = (
        (
            "Person Information",
            {
                "fields": ("user"),
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
