"""
Authentication module for the application.
"""

from .token import TokenAuthentication
from .permission import register_permission
from .auth import get_authentication_classes

__all__ = [
    "register_permission",
    "TokenAuthentication",
    "get_authentication_classes",
]
