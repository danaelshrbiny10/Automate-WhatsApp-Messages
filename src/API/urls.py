"""API App urls."""

from django.urls import path
from API.views import (
    ChatListAPIView,
    ChatDetailAPIView,
    GroupListAPIView,
    GroupDetailAPIView,
)


urlpatterns = [
    path("chats/", ChatListAPIView.as_view(), name="chat_list_api"),
    path("chats/<int:pk>/", ChatDetailAPIView.as_view(), name="chat_detail_api"),
    path("groups/", GroupListAPIView.as_view(), name="group-list"),
    path("groups/<int:pk>/", GroupDetailAPIView.as_view(), name="group-detail"),
]
