"""API App urls."""

from django.urls import path
from API.views import ChatListAPIView, ChatDetailAPIView


urlpatterns = [
    path("chats/", ChatListAPIView.as_view(), name="chat_list_api"),
    path("chats/<int:pk>/", ChatDetailAPIView.as_view(), name="chat_detail_api"),
    
]
