"""API App views."""

from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from datetime import timedelta
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins, generics
from API.models import Chat, Group, Feedback
from .serializers import ChatSerializer, GroupSerializer, FeedbackSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .tasks import process_chat, process_group
from django.utils import timezone
from rest_framework.views import exception_handler

import logging

logger = logging.getLogger(__name__)


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

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def get(self, request, *args, **kwargs):
        """Override list method."""
        queryset = self.get_queryset()

        for chat in queryset:
            try:
                process_chat.delay(chat.id)
            except Exception as e:
                logger.error(
                    f"An error occurred while processing chat ID {chat.id}: {e}"
                )

        return super().list(request, *args, **kwargs)


class ChatDetailAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """View to retrieve a specific chat."""

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    lookup_field = "pk"
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60))  # Cache for 1 hour
    def get(self, request, *args, **kwargs):
        """Send GET request."""
        return super().get(request, *args, **kwargs)


class GroupListAPIView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    """View to list all groups and create a new group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def get(self, request, *args, **kwargs):
        """Send GET request to list all groups."""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Send POST request to create a new group."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        group = serializer.save()

        try:
            process_group.apply_async(
                args=[group.id], eta=timezone.now() + timedelta(seconds=10)
            )
        except Exception as e:
            logger.error(f"An error occurred while processing group ID {group.id}: {e}")

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

    @method_decorator(cache_page(60 * 60))  # Cache for 1 hour
    def get(self, request, *args, **kwargs):
        """Send GET request to retrieve a specific group."""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Send PUT request to update a specific group."""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Send DELETE request to delete a specific group."""
        return self.destroy(request, *args, **kwargs)


def custom_exception_handler(exc, context):
    """Custom exception handler for API views."""
    response = exception_handler(exc, context)

    if response is not None:
        logger.error(
            f"An exception occurred: {exc}, status_code: {response.status_code}, data: {response.data}"
        )

    return response



class FeedbackAPIView(APIView):
    """View to list user feedback."""

    def get(self, request, *args, **kwargs):
        """Retrieve a list of all feedbacks."""
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Create a new feedbacks."""
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)