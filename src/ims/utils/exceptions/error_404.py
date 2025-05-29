"""
Custom 404 error handler.
This function generates a JSON response with a 404 status code
"""

from rest_framework import status


from utils.messages import error
from utils.response import generate_response


def error_404(*args, **kwargs):
    """
    Custom 404 error handler.
    This function generates a JSON response with a 404 status code
    """
    return generate_response(
        status_code=status.HTTP_404_NOT_FOUND,
        errors={"message": error.RESOURCE_NOT_FOUND},
        create_json_response=True,
    )
