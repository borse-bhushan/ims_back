"""
This module defines paths to be excluded from processing.
It provides functions to add paths to the exclusion list and check if a path is excluded.
It's useful in middleware that need to skip certain paths
"""

from utils.constants import BASE_PATH

EXLUDE_PATHS = []


def add_excluded_path(path, add_base_path=True):
    """
    Add a path to the list of excluded paths.

    Args:
        path (str): The path to be excluded.
    """
    if path not in EXLUDE_PATHS:
        EXLUDE_PATHS.append(BASE_PATH + path if add_base_path else path)

    return path


def is_path_excluded(path):
    """
    Check if a path is excluded.

    Args:
        path (str): The path to check.

    Returns:
        bool: True if the path is excluded, False otherwise.
    """
    return path in EXLUDE_PATHS
