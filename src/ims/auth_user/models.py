"""
This module defines the models related to user authentication and authorization for the application.

Models:
    - User: Represents an application user, including their personal information, role, and authentication details.
    - Permission: Defines specific permissions (actions) that can be assigned to roles, such as 'can_view_users' or 'can_edit_users'.
    - RolePermissionMapping: Maps roles to permissions, enabling role-based access control.
    - Token: Stores login session tokens associated with users for authentication purposes.
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from utils.functions import get_uuid
from base.db_models.model import BaseModel

from .constants import RoleEnum
from .constants import MethodEnum


class User(BaseModel, AbstractBaseUser):
    __doc__ = """
        This is the model for the application user and there roles.
    """

    user_id = models.CharField(primary_key=True, max_length=64, default=get_uuid)

    email = models.EmailField(unique=True)
    last_name = models.CharField(max_length=128, null=True, default=None)
    first_name = models.CharField(max_length=128, null=True, default=None)
    phone_number = models.CharField(max_length=128, null=True, default=None)

    profile_photo = models.CharField(max_length=512, null=True, default=None)
    password = models.CharField(max_length=128, null=True, default=None)
    date_joined = models.DateTimeField(null=True, default=None)

    role_id = models.CharField(choices=RoleEnum.choices, max_length=64)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    PROFILE_PATH = "/user-profile-img/{file_name}"

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "auth_users"

    @property
    def get_full_name(self):
        """
        Returns the full name of the user
        """
        return f"{self.first_name} {self.last_name}".title()

    def to_dict(self):
        """
        Returns the dict with specific fields
        """
        return {
            "email": self.email,
            "user_id": self.user_id,
            "role_id": self.role_id,
            "phone_number": self.phone_number,
            "profile_photo": self.profile_photo,
            "last_name": f"{self.last_name or ''}".title(),
            "first_name": f"{self.first_name or ''}".title(),
            "full_name": f"{self.get_full_name or ''}".title(),
        }


class Permission(BaseModel, models.Model):
    """
    Permission model to define actions like 'can_view_users', 'can_edit_users', etc.
    Each permission is linked to a module and action.
    """

    permission_id = models.CharField(max_length=64, primary_key=True, default=get_uuid)

    name = models.CharField(max_length=64)
    module = models.CharField(max_length=64)
    action = models.CharField(max_length=64, choices=MethodEnum.choices)

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "permissions"

    def to_dict(self):
        """
        Convert Permission model instance to a dictionary representation.
        Returns:
            dict: A dictionary containing the permission details with the following keys:
                - name (str): The name of the permission
                - module (str): The module this permission belongs to
                - action (str): The action type of the permission
                - permission_id (int): The unique identifier of the permission
        """

        return {
            "name": self.name,
            "module": self.module,
            "action": self.action,
            "permission_id": self.permission_id,
        }


class RolePermissionMapping(BaseModel, models.Model):
    """
    Model to link roles to permissions.
    Useful for tracking role permissions mapping over time.
    """

    role_permission_mapping_id = models.CharField(
        max_length=64, primary_key=True, default=get_uuid
    )

    role_id = models.CharField(choices=RoleEnum.choices, max_length=64)
    permission = models.ForeignKey("Permission", on_delete=models.CASCADE)

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "role_permission_mappings"

    def to_dict(self):
        """
        Convert the model instance to a dictionary.
        Returns:
            dict: Dictionary representation of the model instance.
        """
        return {
            "role_id": self.role_id,
            "permission_id": self.permission_id,
        }


class Token(BaseModel, models.Model):
    """
    Model to save login session token against a user.
    """

    created_dtm = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=512, primary_key=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "token"

    def to_dict(self):
        """
        Convert the Token instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the Token instance.
        """
        return {
            "token": self.token,
            "created_dtm": self.created_dtm,
        }
