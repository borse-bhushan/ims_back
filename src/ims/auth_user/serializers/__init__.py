"""
Serializers for the auth_user app.
"""

from .auth import LoginSerializer
from .user import UserSerializer, UserCompanyAdminSerializer

from .role_permission import RolePermissionSerializer
from .user_query import UserCompanyAdminListQuerySerializer
from .permission_query import PermissionListQuerySerializer

from .swagger import (
    LoginResponseSerializer,
    LogoutResponseSerializer,
    login_success_example,
    logout_success_example,
)

__all__ = [
    "LoginSerializer",
    "UserSerializer",
    "LoginResponseSerializer",
    "LogoutResponseSerializer",
    "login_success_example",
    "logout_success_example",
    "RolePermissionSerializer",
    "UserCompanyAdminListQuerySerializer",
    "UserCompanyAdminSerializer",
    "PermissionListQuerySerializer",
]
