"""
This module provides a function to get authentication classes for the API views.
"""

import importlib

from utils import settings
from utils.messages import error
from utils.exceptions import BadRequestError

from tenant.constants import AuthenticationTypeEnum
from tenant.utils.helpers import is_request_tenant_aware
from tenant.db_access import tenant_configuration_manager

from .jwt_token import JWTAuthentication


def import_authentication_class(class_name):
    """
    This function imports the authentication class based on the provided class name.
    The class name should be in the format 'module.ClassName'.
    """

    module_name = ".".join(class_name.split(".")[:-1])

    # Import the module relative to the current package
    current_module = importlib.import_module(module_name, __package__)

    auth_class_name = class_name.split(".")[-1]
    return current_module.__dict__[auth_class_name]


def get_default_authentication_class(*_, **__):
    """
    This function returns the default authentication class object to be used in the API views.
    """

    str_auth_class = settings.read("DEFAULT_AUTHENTICATION_CLASSES")

    return [import_authentication_class(class_name)() for class_name in str_auth_class]


def get_jwt_authentication_class(*_, **__):
    """
    This function returns the JWT authentication class object to be used in the API views.
    """

    return [JWTAuthentication()]


def get_authentication_classes(*_, **__):
    """
    This function returns a list of authentication classes to be used in the API views.
    The authentication classes are used to authenticate users and provide access control.
    """

    if not is_request_tenant_aware():
        return get_default_authentication_class()

    tenant_configuration_obj = tenant_configuration_manager.get({})

    if not tenant_configuration_obj:
        raise BadRequestError(error.TENANT_CONFIGURATION_NOT_FOUND)

    if tenant_configuration_obj.authentication_type == AuthenticationTypeEnum.TOKEN:
        return get_default_authentication_class()

    if tenant_configuration_obj.authentication_type == AuthenticationTypeEnum.JWT_TOKEN:
        return [JWTAuthentication()]

    raise BadRequestError(error.AUTHENTICATION_NOT_CONFIGURED)
