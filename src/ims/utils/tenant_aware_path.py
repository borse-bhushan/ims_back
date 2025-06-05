"""
Utility functions to manage tenant-aware excluded paths.
"""

from utils.constants import BASE_PATH

EXLUDE_PATHS = {}


class AllMethods:
    """
    A class representing all HTTP methods.
    """

    pass


def add_to_tenant_aware_excluded_path_list(
    _path, add_base_path=True, other_base_path="", method_list=AllMethods
):
    """
    Add a path to the list of excluded paths.

    Args:
        path (str): The path to be excluded.
    """
    path = other_base_path + _path

    if path not in EXLUDE_PATHS:
        e_path = BASE_PATH + path if add_base_path else path

        if method_list is AllMethods:
            EXLUDE_PATHS[e_path] = AllMethods
        else:
            EXLUDE_PATHS[e_path] = [method.upper() for method in method_list]

    return _path


def is_path_excluded_from_tenant_aware(path: str, method: str):
    """
    Check if a path is excluded.

    Args:
        path (str): The path to check.

    Returns:
        bool: True if the path is excluded, False otherwise.
    """

    e_methods = EXLUDE_PATHS.get(path)
    if e_methods is None:
        return False

    if e_methods is AllMethods:
        return True

    return method.upper() in e_methods
