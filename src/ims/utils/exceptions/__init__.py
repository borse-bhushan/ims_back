"""
This module contains custom exceptions for the application.
"""

from .error_404 import error_404

from .exceptions import (
    CommonError,
    SettingKeyError,
    ValidationError,
    BadRequestError,
    NoDataFoundError,
    PermissionDenied,
)


__all__ = [
    "error_404",
    "CommonError",
    "SettingKeyError",
    "NoDataFoundError",
    "ValidationError",
    "BadRequestError",
    "PermissionDenied",
]
