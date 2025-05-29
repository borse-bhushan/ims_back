"""
This module provides a utility function to format Django Rest Framework (DRF)
serializer errors into a more user-friendly format.
It recursively processes the errors, handling nested serializers and list serializers,
and formats them into a list of dictionaries with a "message" key.
The formatted errors can be used in API responses to provide clear feedback
to the client about validation issues.
"""

import re

from utils.exceptions import codes


def format_serializer_errors(errors, parent_field="", input_data=None):
    """
    Recursively formats DRF serializer errors into a list of {"message": "..."} dicts.
    Handles nested serializers, list serializers, and non_field_errors.

    Args:
        errors (dict | list): DRF ValidationError detail.
        parent_field (str): Used for nested field naming.

    Returns:
        list[dict]: List of formatted error messages.
    """

    formatted = []

    if isinstance(errors, dict):
        for field, value in errors.items():
            full_field = f"{parent_field}.{field}" if parent_field else field
            next_input = input_data.get(field) if isinstance(input_data, dict) else None
            formatted += format_serializer_errors(value, full_field, next_input)

    elif isinstance(errors, list):
        for item in errors:
            if isinstance(item, (dict, list)):
                formatted += format_serializer_errors(item, parent_field, input_data)
            else:
                code = getattr(item, "code", codes.INVALID).upper()
                message = str(item)

                error_entry = {
                    "code": code,
                    "message": message,
                    "field": parent_field,
                }

                # Extract limits
                nums = [int(n) for n in re.findall(r"\d+", message)]
                if "MAX" in code and nums:
                    error_entry["max_limit"] = nums[0]
                elif "MIN" in code and nums:
                    error_entry["min_limit"] = nums[0]
                elif "EXACT" in code and nums:
                    error_entry["expected"] = nums[0]

                if input_data is not None:
                    error_entry["user_value"] = input_data

                formatted.append(error_entry)

    return formatted
