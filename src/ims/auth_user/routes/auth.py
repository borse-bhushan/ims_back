"""
URL patterns for authentication endpoints.

This module defines the URL patterns for authentication-related views.
It includes endpoints for user login and logout operations.

URLs:
    - /login: POST request to authenticate and login a user
    - /logout: DELETE request to logout a currently authenticated user

"""

from django.urls import path

from auth_user.views import (
    LoginViewSet,
    LogoutViewSet,
)


urlpatterns = [
    path(
        "login",
        LoginViewSet.as_view(LoginViewSet.get_method_view_mapping()),
        name="login",
    ),
    path(
        "logout",
        LogoutViewSet.as_view(LogoutViewSet.get_method_view_mapping()),
        name="logout",
    ),
]
