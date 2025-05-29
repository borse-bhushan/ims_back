"""
This module contains the base exception class for all custom exceptions
"""

from utils.exceptions import codes


class BaseExc(Exception):
    """
    Base Exception class for all custom exceptions
    """

    code = codes.UNKNOWN_ERROR

    def __init__(
        self, message: str, status_code: int, code: str = None, ref_data: dict = None
    ):

        self.message = message
        self.ref_data = ref_data
        self.code = code or self.code
        self.status_code = status_code

    def __str__(self):
        return self.message
