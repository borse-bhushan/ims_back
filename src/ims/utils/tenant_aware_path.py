"""
Utility functions to manage tenant-aware excluded paths.
"""

from utils.constants import BASE_PATH

EXLUDE_PATHS = []


def add_to_tenant_aware_excluded_path_list(
    _path, add_base_path=True, other_base_path=""
):
    """
    Add a path to the list of excluded paths.

    Args:
        path (str): The path to be excluded.
    """
    path = other_base_path + _path

    if path not in EXLUDE_PATHS:
        EXLUDE_PATHS.append(BASE_PATH + path if add_base_path else path)

    return _path


def is_path_excluded_from_tenant_aware(path):
    """
    Check if a path is excluded.

    Args:
        path (str): The path to check.

    Returns:
        bool: True if the path is excluded, False otherwise.
    """

    return path in EXLUDE_PATHS
