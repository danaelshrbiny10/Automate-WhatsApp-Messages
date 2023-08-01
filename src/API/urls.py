"""API App urls."""

from django.urls import path
from API.views import (
    ChatListAPIView,
    ChatDetailAPIView,
    GroupListAPIView,
    GroupDetailAPIView,
    FeedbackAPIView
)


urlpatterns = [
    path("chats/", ChatListAPIView.as_view(), name="chat_list_api"),
    path("chats/<int:pk>/", ChatDetailAPIView.as_view(), name="chat_detail_api"),
    path("groups/", GroupListAPIView.as_view(), name="group_list"),
    path("groups/<int:pk>/", GroupDetailAPIView.as_view(), name="group_detail"),
    path('feedback/', FeedbackAPIView.as_view(), name='feedback-list'),
]
