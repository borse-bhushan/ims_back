"""
Validation Module for Unique Records.
This module provides functionality to validate uniqueness of records in a database.
It contains utilities to check if a record with specific attributes already exists,
helping to prevent duplicate entries in the database.
# Check if user with email already exists
validate_unique(User.objects, {"email": "test@example.com"})
"""

from rest_framework import serializers

from base.db_access import Manager

from ..messages import error
from ..exceptions import codes


def validate_unique(model_manager: Manager, query: dict):
    """
    Validates uniqueness of a record based on given query parameters.
    This function checks if a record already exists in the database
    using the provided query parameters.
    If a matching record is found, it raises a ValidationError indicating duplicate entry.
    Args:
        model_manager (Manager): The model manager instance used to query the database
        query (dict): Dictionary containing the query parameters to check uniqueness
    Returns:
        bool: True if no matching record exists
    Raises:
        ValidationError: If a record matching the query already exists in the database
    Example:
        >>> validate_unique(User.objects, {"email": "test@example.com"})
        True
    """

    if model_manager.exists(query=query):
        raise serializers.ValidationError(
            error.ALREADY_EXIST,
            code=codes.DUPLICATE_ENTRY,
        )

    return True
