"""
User serializers module.
"""

from .user import (
    UserResponseSerializer,
    UserListResponseSerializer,
    user_create_success_example,
    user_list_success_example,
    user_get_by_id_success_example,
    user_update_success_example,
    user_delete_success_example
)

from .role import (
    RoleResponseSerializer,
    RoleListResponseSerializer,
    role_create_success_example,
    role_list_success_example,
    role_get_by_id_success_example,
    role_update_success_example,
    role_delete_success_example
)

from .permission import (
    PermissionResponseSerializer,
    PermissionListResponseSerializer,
    permission_create_success_example,
    permission_list_success_example,
    permission_get_by_id_success_example,
    permission_update_success_example,
    permission_delete_success_example
)

from .user_role import (
    UserRoleResponseSerializer,
    UserRoleListResponseSerializer,
    user_role_create_success_example,
    user_role_list_success_example,
    user_role_delete_success_example
)

from .role_permission import (
    RolePermissionResponseSerializer,
    RolePermissionListResponseSerializer,
    role_permission_create_example,
    role_permission_list_example,
    role_permission_delete_example
)

__all__ = [
    "UserResponseSerializer",
    "UserListResponseSerializer",
    "user_create_success_example",
    "user_list_success_example",
    "user_get_by_id_success_example",
    "user_update_success_example",
    "user_delete_success_example",

    "RoleResponseSerializer",
    "RoleListResponseSerializer",
    "role_create_success_example",
    "role_list_success_example",
    "role_get_by_id_success_example",
    "role_update_success_example",
    "role_delete_success_example",

    "PermissionResponseSerializer",
    "PermissionListResponseSerializer",
    "permission_create_success_example",
    "permission_list_success_example",
    "permission_get_by_id_success_example",
    "permission_update_success_example",
    "permission_delete_success_example",

    "UserRoleResponseSerializer",
    "UserRoleListResponseSerializer",
    "user_role_create_success_example",
    "user_role_list_success_example",
    "user_role_delete_success_example",

    "RolePermissionResponseSerializer",
    "RolePermissionListResponseSerializer",
    "role_permission_create_example",
    "role_permission_list_example",
    "role_permission_delete_example"
]
