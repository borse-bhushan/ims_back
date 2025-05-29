"""
Custom exceptions for the utils module
"""

import json

from rest_framework import status

from base.exceptions import BaseExc

from . import codes
from ..messages import error


class SettingKeyError(BaseExc):
    """
    Exception raised when a key is not found in the settings
    """

    code = codes.SETTING_KEY_NOT_FOUND

    def __init__(self, key, status_code: int, ref_data: dict = None):
        self.key = key
        self.message = f"Key '{key}' not found in settings"
        super().__init__(self.message, status_code, ref_data)

    def __str__(self):
        return self.message


class CommonError(BaseExc):
    """
    Use to raise the general errors
    """


class NoDataFoundError(BaseExc):
    """
    Exception raised when data not found
    """

    code = codes.NO_DATA_FOUND

    def __init__(self, ref_data: dict = None):
        self.message = error.NO_DATA_FOUND
        super().__init__(self.message, status.HTTP_404_NOT_FOUND, ref_data)

    def __str__(self):
        return self.message


class BadRequestError(BaseExc):
    """
    Exception for bad request.
    """

    code = codes.BAD_REQUEST

    def __init__(self, message: str, code: str = None, ref_data: dict = None):
        self.message = message
        super().__init__(self.message, status.HTTP_400_BAD_REQUEST, code, ref_data)

    def __str__(self):
        return self.message


class ValidationError(BaseExc):
    """
    Exception raised when validation fails
    """

    def __init__(
        self,
        details: dict | list,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        ref_data: dict = None,
    ):
        super().__init__(details, status_code, ref_data)

    def __str__(self):

        return f"Validation Error: {json.dumps(self.message)}"


class PermissionDenied(BaseExc):
    """
    Exception raised when permission is denied
    """

    code = codes.PERMISSION_DENIED

    def __init__(self):
        super().__init__(error.PERMISSION_DENIED, status.HTTP_403_FORBIDDEN)

    def __str__(self):
        return f"Permission Denied: {self.message}"
