"""
Exception classes for authentication module.
"""

from rest_framework import status

from utils.messages import error
from utils.exceptions import codes
from base.exceptions import BaseExc


class UnauthorizedException(BaseExc):
    """
    Exception raised when user is not authorized to perform an action.
    """

    code = codes.UNAUTHORIZED

    def __init__(self, ref_data: dict = None):
        self.message = error.UNAUTHORIZED_ACCESS
        super().__init__(self.message, status.HTTP_401_UNAUTHORIZED, ref_data)

    def __str__(self):
        return self.message


class WrongCredentialsException(BaseExc):
    """
    Exception raised when user is not authorized to perform an action.
    """

    code = codes.WRONG_CREDENTIALS

    def __init__(self, ref_data: dict = None):
        self.message = error.WRONG_CREDENTIALS
        super().__init__(self.message, status.HTTP_401_UNAUTHORIZED, ref_data)

    def __str__(self):
        return self.message
