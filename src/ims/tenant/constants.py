"""
Constants for the tenant application.
"""

from django.db.models import TextChoices


class AuthenticationTypeEnum(TextChoices):
    """Enumeration for authentication types."""

    TOKEN = "TOKEN", "Token"
    JWT_TOKEN = "JWT_TOKEN", "JWT Token"


class DatabaseStrategyEnum(TextChoices):

    SHARED = "SHARED", "Shared DB"
    SEPARATE = "SEPARATE", "Separate DB"
