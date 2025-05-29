"""
Auth user related enums
"""

from django.db import models


class RoleEnum(models.TextChoices):
    """
    RoleEnum is a class that defines constants representing different user roles
    within the system. Each role is represented as a string constant.
    """

    SUPER_COMPANY_ADMIN = "SUPER_COMPANY_ADMIN", "SUPER_COMPANY_ADMIN"


class MethodEnum(models.TextChoices):
    """
    Enum for invoice status.
    """

    GET = "GET", "GET"
    POST = "POST", "POST"

    PUT = "PUT", "PUT"
    PATCH = "PATCH", "PATCH"
    DELETE = "DELETE", "DELETE"
