"""
RolePermission-related URL patterns for authentication and permission management.

This module defines URL patterns for role-permission-related operations in the system.
It maps HTTP methods to corresponding view methods in the RolePermissionViewSet.

URL Patterns:
    - /role-permission:
        - GET: List all role-permission mappings
        - POST: Create a new role-permission mapping

    - /role-permission/<str:role_id>/<str:permission_id>:
        - DELETE: Remove a specific role-permission mapping
"""

from django.urls import path

from auth_user.views import RolePermissionViewSet

urlpatterns = [
    path(
        "role-permission",
        RolePermissionViewSet.as_view(RolePermissionViewSet.get_method_view_mapping()),
        name="role-permission",
    ),
    path(
        "role-permission/<str:role_id>/<str:permission_id>",
        RolePermissionViewSet.as_view(
            RolePermissionViewSet.get_method_view_mapping(True)
        ),
        name="role-permission-detail",
    ),
]
