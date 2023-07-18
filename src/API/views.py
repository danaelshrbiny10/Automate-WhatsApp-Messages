"""API App views."""

from rest_framework import mixins, generics
from API.models import Chat, Group
from .serializers import ChatSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .tasks import process_chat


class ChatListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    """View to list all chats."""

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Override get queryset method."""
        name = self.request.query_params.get("name", None)
        if name is not None:
            return self.queryset.filter(name__icontains=name)
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        """Send GET request."""
        queryset = self.get_queryset()

        for chat in queryset:
            process_chat.delay(chat.id)

        return self.list(request, *args, **kwargs)


class ChatDetailAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """View to retrieve a specific chat."""

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    lookup_field = "pk"
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Send GET request."""
        return self.retrieve(request, *args, **kwargs)
