"""
This module contains the views for the auth_user app.
"""

from .permission import PermissionViewSet
from .user import UserViewSet, UserProfileViewSet
from .role_permission import RolePermissionViewSet
from .auth import (
    LoginViewSet,
    LogoutViewSet,
)

__all__ = [
    "UserViewSet",
    "LoginViewSet",
    "LogoutViewSet",
    "PermissionViewSet",
    "UserProfileViewSet",
    "RolePermissionViewSet",
]
