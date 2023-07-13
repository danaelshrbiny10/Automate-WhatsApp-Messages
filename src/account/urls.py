"""Auth App urls."""

from django.urls import path
from account.views import RegistrationView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
