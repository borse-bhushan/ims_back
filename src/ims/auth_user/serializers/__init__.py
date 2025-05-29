"""
Serializers for the auth_user app.
"""

from .user import UserSerializer
from .role import RoleSerializer
from .auth import LoginSerializer
from .swagger import (
    LoginResponseSerializer,
    LogoutResponseSerializer,
    login_success_example,
    logout_success_example
)
from .permission import PermissionSerializer
from .role_permission import RolePermissionSerializer
from .user_role import UserRoleSerializer, UserRoleListQuerySerializer

__all__ = [
    "LoginSerializer",
    "UserSerializer",
    "LoginResponseSerializer",
    "LogoutResponseSerializer",
    "login_success_example",
    "logout_success_example",
    "RoleSerializer",
    "UserRoleSerializer",
    "PermissionSerializer",
    "RolePermissionSerializer",
    "UserRoleListQuerySerializer",
]
