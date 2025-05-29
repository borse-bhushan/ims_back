"""
This module is used to read settings from the Django settings file.
"""

from rest_framework import status
from django.conf import settings as django_settings

from utils.exceptions import SettingKeyError


class Empty:
    """
    This class is used to represent an empty value.
    """


def read(setting_key: str):
    """
    Read the setting from the Django settings file.
    """

    val = getattr(django_settings, setting_key, Empty)

    if val is Empty:
        raise SettingKeyError(
            setting_key,
            status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return val
