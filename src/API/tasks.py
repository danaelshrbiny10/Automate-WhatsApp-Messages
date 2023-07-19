"""API App Task."""

from datetime import timezone
from celery import shared_task
from API.models import Chat, Group


@shared_task
def process_chat(chat_id):
    """Retrieve the Chat object using the provided chat_id."""
    chat = Chat.objects.get(id=chat_id)
    chat.last_messaged_time = timezone.now()
    chat.save()

@shared_task
def process_group(group_id):
    """Retrieve the Group object using the provided group_id."""
    try:
        group = Group.objects.get(id=group_id)
        print(f"Processing group: {group.title}")
    except Group.DoesNotExist:
        print(f"Group with ID {group_id} does not exist")
