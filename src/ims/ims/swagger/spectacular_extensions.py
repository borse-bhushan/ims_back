"""
A custom authentication scheme extension for drf-spectacular.
"""

from drf_spectacular.extensions import OpenApiAuthenticationExtension


from utils import settings


class CustomTokenAuthScheme(OpenApiAuthenticationExtension):
    """
    This class extends OpenApiAuthenticationExtension to provide a custom token-based
    authentication scheme for API documentation. It defines the security scheme as
    an HTTP Bearer token authentication.

    Attributes:
        target_class (str): The full dotted path to the authentication class.
        name (str): The name of the security scheme used in SPECTACULAR_SETTINGS.

    Example:
        To use this authentication scheme, include it in your SPECTACULAR_SETTINGS:
        SPECTACULAR_SETTINGS = {
            "SECURITY": [{"TokenAuth": []}]

    """

    target_class = settings.read("TOKEN_AUTHENTICATION_CLASS")
    name = "TokenAuth"  # must match the name used in SPECTACULAR_SETTINGS["SECURITY"]

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "Token",  # or JWT, depending on your format
        }
