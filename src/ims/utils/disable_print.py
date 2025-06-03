"""
This file contains the function to disable the print function.
"""

import builtins
import traceback

from rest_framework import status

from utils.messages import error
from utils.exceptions import CommonError


def disable_print():
    """
    Disables the print function across the Django project except in virtual environment packages.
    """
    original_print = builtins.print  # Store the original print function

    def restricted_print(*args, **kwargs):
        stack = traceback.extract_stack()
        caller = stack[-2]  # Get the second-last frame (where 'print' was called from)
        caller_file = caller.filename

        # Allow print only for virtual environment packages
        if "site-packages" in caller_file or "venv" in caller_file:
            original_print(*args, **kwargs)
        else:
            raise CommonError(
                message=error.PRINT_FUNCTION_IS_DISABLE,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    builtins.print = restricted_print  # Override the global print function
