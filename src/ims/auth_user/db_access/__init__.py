"""
This module imports and initializes the data access layer (DAL) components for the
authentication system. It includes managers for roles, users, permissions, and their mappings.
Each manager provides an interface to interact with the corresponding model and perform
"""

from .role import role_manager
from .user import user_manager
from .token import token_manager
from .permission import permission_manager
from .user_role_mapping import user_role_mapping_manager
from .role_permission_mapping import role_permission_mapping_manager

__all__ = [
    "role_manager",
    "user_manager",
    "token_manager",
    "permission_manager",
    "user_role_mapping_manager",
    "role_permission_mapping_manager",
]
