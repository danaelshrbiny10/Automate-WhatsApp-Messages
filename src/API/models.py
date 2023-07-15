"""API app models."""

from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel


class Chat(TimeStampedModel):
    """Chat model for storing chat information in the database including details about the user, chat name, message content, timestamps, and unread message count.

    user: This field is a foreign key to the User model, indicating the user associated with the chat.
    name: This field represents the name or title of the chat conversation, limited to a maximum of 20 characters.
    is_groupchat: This boolean field indicates whether the chat is a group chat or a one-on-one conversation.
    messages: This field stores the messages exchanged in the chat as a string, limited to a maximum of 2000 characters.
    phone_number: This field stores the phone number associated with the chat conversation, limited to a maximum of 20 characters.
    last_messaged_time: This field represents the timestamp of the most recent message in the chat.
    unread_messages_count: This field stores the count of unread messages in the chat, with a default value of 0.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    is_groupchat = models.BooleanField(default=False)
    messages = models.CharField(max_length=2000)
    phone_number = models.CharField(max_length=20)
    last_messaged_time = models.DateTimeField(blank=True, null=True)
    unread_messages_count = models.IntegerField(default=0)

    def __str__(self)  -> str:
        """Override the default string representation of an instance of the model."""
        return self.name

    class Meta:
        """Metadata for the model."""

        verbose_name = "Chat"
        verbose_name_plural = "Chats"


class Group(TimeStampedModel):
    """Group model provides a structure for storing information about group chats, including details such as the title, description, members, administrator, image, privacy settings, and password.

    title: This field represents the title or name of the group chat, limited to a maximum of 50 characters.
    description: This field stores a text description of the group chat.
    members: This field is a many-to-many relationship with the User model, allowing multiple users to be members of the group. The related_name attribute is set to 'user_groups'.
    image: This field stores an image associated with the group chat. It uses the ImageField to handle image uploads.
    admin: This field is a foreign key to the User model, indicating the administrator of the group. The related_name attribute is set to 'admin_groups'.
    slug: This field stores a unique slug for the group chat, which can be used for generating URLs or identifying the group in a user-friendly way.
    password: This field stores the password for accessing the group chat, limited to a maximum of 16 characters.
    private: This boolean field indicates whether the group chat is private or public.
    invite_only: This boolean field indicates whether the group chat is invite-only or open to anyone.
    allow_anonymous: This boolean field indicates whether anonymous users are allowed to join the group chat.
    """

    title = models.CharField(max_length=50)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name="user_groups", blank=True)
    image = models.ImageField(upload_to="images/", default="", null=True, blank=True)
    admin = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="admin_groups"
    )
    slug = models.SlugField(unique=True)
    password = models.CharField(max_length=16, verbose_name="Password")
    private = models.BooleanField(default=False, verbose_name="Private")
    invite_only = models.BooleanField(default=False, verbose_name="Invite Only")
    allow_anonymous = models.BooleanField(
        default=False, verbose_name="Allow Anonymous Users to Join?"
    )

    def __str__(self) -> str:
        """Override the default string representation of an instance of the model."""
        return self.title

    class Meta:
        """Metadata for the model."""

        verbose_name = "Group"
        verbose_name_plural = "Groups"
