"""
This file contains the constants used for the utility.
"""

from django.db.models import TextChoices

PROD = "PROD"
LOCAL = "LOCAL"


CMD = "ver"
VERSION_TYPE = "part"

MAJOR_VERSION = "MJ"
MINOR_VERSION = "MN"
BUG_FIX = "BF"
CURRENT_VERSION = "CV"


BASE_PATH = "api/"


class SeverityEnum(TextChoices):
    """
    Enum for notification severity levels.
    """

    LOW = "LOW", "Low"
    MEDIUM = "MEDIUM", "Medium"
    HIGH = "HIGH", "High"
    CRITICAL = "CRITICAL", "Critical"
    INFO = "INFO", "Info"
    WARNING = "WARNING", "Warning"
    ERROR = "ERROR", "Error"
