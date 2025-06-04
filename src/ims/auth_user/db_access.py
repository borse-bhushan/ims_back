"""
Database access layer for the authentication user module.
"""

from base.db_access import manager
from .models import User, Token, Permission, RolePermissionMapping


class UserManager(manager.Manager[User]):
    """
    Manager class for the User model.
    """

    model = User


class PermissionManager(manager.Manager[Permission]):
    """
    Manager class for the Permission model.
    """

    model = Permission


class RolePermissionMappingManager(manager.Manager[RolePermissionMapping]):
    """
    Manager class for the RolePermissionMapping model.
    """

    model = RolePermissionMapping


class TokenManager(manager.Manager[Token]):
    """
    Manager class for the Token model.
    """

    model = Token
    check_is_deleted: bool = False


user_manager = UserManager()
token_manager = TokenManager()
permission_manager = PermissionManager()
role_permission_mapping_manager = RolePermissionMappingManager()
