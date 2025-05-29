"""
This module provides a function to get authentication classes for the API views.
"""
import importlib
from utils import settings


def get_authentication_classes():
    """
    This function returns a list of authentication classes to be used in the API views.
    The authentication classes are used to authenticate users and provide access control.
    """

    str_auth_classes = settings.read("AUTHENTICATION_CLASSES")

    auth_classes = []
    for str_auth_class in str_auth_classes:
        auth_classes.append(
            importlib.import_module(
                ".".join(str_auth_class.split(".")[:-1]), __package__
            ).__dict__[str_auth_class.split(".")[-1]]
        )

    return auth_classes
