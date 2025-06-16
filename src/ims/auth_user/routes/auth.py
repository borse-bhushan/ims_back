"""
URL patterns for authentication endpoints.

This module defines the URL patterns for authentication-related views.
It includes endpoints for user login and logout operations.

URLs:
    - /login: POST request to authenticate and login a user
    - /logout: DELETE request to logout a currently authenticated user

"""

from django.urls import path

from utils.tenant_aware_path import add_to_tenant_aware_excluded_path_list

from auth_user.views import LoginViewSet, LogoutViewSet


urlpatterns = [
    path(
        "login",
        LoginViewSet.as_view(LoginViewSet.get_method_view_mapping()),
        name="login",
    ),
    path(
        add_to_tenant_aware_excluded_path_list("admin/login", other_base_path="auth/"),
        LoginViewSet.as_view(LoginViewSet.get_method_view_mapping()),
        name="login",
    ),
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
    path(
        add_to_tenant_aware_excluded_path_list("admin/logout", other_base_path="auth/"),
        LogoutViewSet.as_view(LogoutViewSet.get_method_view_mapping()),
        name="logout",
    ),
]
