"""
User-related URL patterns for authentication and user management.

This module defines URL patterns for user-related operations in the authentication system.
It maps HTTP methods to corresponding view methods in the UserViewSet.

URL Patterns:
    - /user:
        - GET: List all users
        - POST: Create a new user

    - /user/<str:user_id>:
        - GET: Retrieve a specific user's details
        - PUT: Full update of a user's information
        - PATCH: Partial update of a user's information
        - DELETE: Remove a user

Note:
    All paths are relative to the base API URL.

"""

from django.urls import path

from auth_user.views import UserViewSet, UserProfileViewSet

urlpatterns = [
    path(
        "user/profile",
        UserProfileViewSet.as_view(UserProfileViewSet.get_method_view_mapping()),
        name="user-profile",
    ),
    path(
        "user", UserViewSet.as_view(UserViewSet.get_method_view_mapping()), name="User"
    ),
    path(
        "user/<str:user_id>",
        UserViewSet.as_view(UserViewSet.get_method_view_mapping(True)),
        name="user-detail",
    ),
]
