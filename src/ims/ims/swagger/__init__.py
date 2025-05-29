"""
Module for authentication schema configuration.

This module provides functionality for configuring custom authentication schema
used in API documentation and the Swagger UI.

Classes:
    CustomTokenAuthScheme: A custom authentication scheme for token-based authentication.

Functions:
    get_token_auth_schema(): Returns the custom token authentication scheme class.

The module primarily supports the integration of custom token-based authentication
with drf-spectacular for OpenAPI schema generation.

"""

from .spectacular_extensions import CustomTokenAuthScheme


__all__ = ["CustomTokenAuthScheme"]


def get_token_auth_schema():
    """
    Returns the CustomTokenAuthScheme class for token-based authentication.
    This function provides the authentication schema class used for token-based
    authentication in the API endpoints. The CustomTokenAuthScheme handles the validation
    and processing of authentication tokens.
    Returns:
        class: The CustomTokenAuthScheme class used for token authentication
    """
    return CustomTokenAuthScheme
