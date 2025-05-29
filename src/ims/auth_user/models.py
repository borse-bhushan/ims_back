"""
This module contains the User model for the application.
It defines the fields and methods for the User model.
The User model is used to store user information and authentication details.

"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from utils.functions import get_uuid
from base.db_models.model import BaseModel
from tenant.db_access import tenant_manager

from auth_user.constants import RoleEnum


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
            "phone_number": self.phone_number,
            "profile_photo": self.profile_photo,
            "last_name": f"{self.last_name or ''}".title(),
            "first_name": f"{self.first_name or ''}".title(),
            "full_name": f"{self.get_full_name or ''}".title(),
        }

    @property
    def tenant(self):
        """
        Returns the tenant id of the user
        """
        return tenant_manager.get({"tenant_id": self.tenant_id})
