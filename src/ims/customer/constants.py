"""
Constants for Customer Management
"""

from django.db.models import TextChoices


class SSOProvideEnum(TextChoices):
    """SSO Provider Enum"""

    GOOGLE = "GOOGLE", "Google"
    MICROSOFT = "MICROSOFT", "Microsoft"


class TenantIDEnum(TextChoices):
    """Microsoft Tenant Identifier Enum"""

    COMMON = "common", "All Accounts (common)"
    ORGANIZATIONS = "organizations", "Work/School Only (organizations)"
    CONSUMERS = "consumers", "Personal Microsoft Accounts Only (consumers)"
