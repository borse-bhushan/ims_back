"""
URL configuration for the auth_user app.
"""

from django.urls import path, include

urlpatterns = [
    path("auth/", include("auth_user.routes.auth")),
    path("", include("auth_user.routes.user")),
    path("", include("auth_user.routes.permission")),
    path("", include("auth_user.routes.role_permission")),
]
