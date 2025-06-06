"""
Permission-related URL patterns for authentication and permission management.

This module defines URL patterns for permission-related operations in the authentication system.
It maps HTTP methods to corresponding view methods in the PermissionViewSet.

URL Patterns:
    - /permission:
        - GET: List all permissions
        - POST: Create a new permission

    - /permission/<str:permission_id>:
        - GET: Retrieve a specific permission's details
        - PUT: Full update of a permission's information
        - PATCH: Partial update of a permission's information
        - DELETE: Remove a permission

Note:
    All paths are relative to the base API URL.
"""

from django.urls import path

from utils.tenant_aware_path import add_to_tenant_aware_excluded_path_list

from auth_user.constants import MethodEnum
from auth_user.views import PermissionViewSet

urlpatterns = [
    path(
        add_to_tenant_aware_excluded_path_list(
            "permission", method_list=[MethodEnum.POST]
        ),
        PermissionViewSet.as_view(PermissionViewSet.get_method_view_mapping()),
        name="permission",
    ),
    path(
        "permission/<str:permission_id>",
        PermissionViewSet.as_view(PermissionViewSet.get_method_view_mapping(True)),
        name="permission-detail",
    ),
]
