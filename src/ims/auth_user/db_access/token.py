"""
Token Manager
This module contains the manager for the Token model.
It provides an interface to interact with the Token model and perform
"""

from base.db_access import manager

from ..db_models import Token


class TokenManager(manager.Manager[Token]):
    """
    Manager class for the Token model.
    """

    model = Token
    check_is_deleted: bool = False


token_manager = TokenManager()
