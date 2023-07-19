"""API App views."""


from datetime import timedelta
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins, generics
from API.models import Chat, Group
from .serializers import ChatSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .tasks import process_chat, process_group
from django.utils import timezone


class ChatListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    """View to list all chats."""

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Override get queryset method."""
        name = self.request.query_params.get("name", None)
        if name is not None:
            return self.queryset.filter(name__icontains=name)
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        """Override list method."""
        queryset = self.get_queryset()

        for chat in queryset:
            process_chat.delay(chat.id)

        return super().list(request, *args, **kwargs)


class ChatDetailAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """View to retrieve a specific chat."""

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    lookup_field = "pk"
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        """Override retrieve method."""
        return super().retrieve(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """Send GET request."""
        return self.retrieve(request, *args, **kwargs)


class GroupListAPIView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    """View to list all groups and create a new group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Send GET request to list all groups."""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Send POST request to create a new group."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        group = serializer.save()

        process_group.apply_async(args=[group.id], eta=timezone.now() + timedelta(seconds=10))

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GroupDetailAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """View to retrieve, update, and delete a specific group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Send GET request to retrieve a specific group."""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Send PUT request to update a specific group."""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Send DELETE request to delete a specific group."""
        return self.destroy(request, *args, **kwargs)
