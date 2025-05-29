"""
Role-related URL patterns for authentication and role management.

This module defines URL patterns for role-related operations in the authentication system.
It maps HTTP methods to corresponding view methods in the RoleViewSet.

URL Patterns:
    - /role:
        - GET: List all roles
        - POST: Create a new role

    - /role/<str:role_id>:
        - GET: Retrieve a specific role's details
        - PUT: Full update of a role's information
        - PATCH: Partial update of a role's information
        - DELETE: Remove a role

Note:
    All paths are relative to the base API URL.
"""

from django.urls import path

from ..views import UserRoleViewSet

urlpatterns = [
    path(
        "user-role",
        UserRoleViewSet.as_view(UserRoleViewSet.get_method_view_mapping()),
        name="user-role",
    ),
    path(
        "user-role/<str:user_id>/<str:role_id>",
        UserRoleViewSet.as_view(UserRoleViewSet.get_method_view_mapping(True)),
        name="user-role-detail",
    ),
]
