"""
Auth user related enums
"""

from django.db import models


class RoleEnum(models.TextChoices):
    """
    RoleEnum is a class that defines constants representing different user roles
    within the system. Each role is represented as a string constant.
    """

    SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"

    COMPANY_ADMIN = "COMPANY_ADMIN", "Company Admin"
    MANAGER = "MANAGER", "Manager"
    OPERATOR = "OPERATOR", "Operator"


class MethodEnum(models.TextChoices):
    """
    Enum for invoice status.
    """

    # Without ID
    GET = "GET", "GET"
    POST = "POST", "POST"

    # With ID
    PUT = "PUT", "PUT"
    PATCH = "PATCH", "PATCH"
    DELETE = "DELETE", "DELETE"
