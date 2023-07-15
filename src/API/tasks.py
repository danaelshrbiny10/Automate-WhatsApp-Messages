"""API App Task."""

from datetime import timezone
from celery import shared_task
from API.models import Chat


@shared_task
def process_chat(chat_id):
    """Retrieve the Chat object using the provided chat_id."""
    chat = Chat.objects.get(id=chat_id)
    chat.last_messaged_time = timezone.now()
    chat.save()
