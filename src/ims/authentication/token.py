"""
Token authentication for the API.
This module provides a class that implements token-based authentication for API requests.
"""

from rest_framework.authentication import BaseAuthentication

from utils.functions import get_current_datetime

from auth_user.db_access import token_manager

from .exception import UnauthorizedException


class TokenAuthentication(BaseAuthentication):
    """
    Token authentication class for API views.
    This class is used to authenticate users based on a token provided in the request headers.
    """

    keyword = "Bearer"

    def authenticate(self, request):
        """
        Authenticate the user based on the token provided in the request headers.
        If the token is valid, return the user and token objects.
        If the token is invalid or missing, raise an UnauthorizedException.
        """

        auth_token = request.headers.get("Authorization") or ""

        if not auth_token:
            raise UnauthorizedException()

        auth_token_arr = auth_token.split(" ")

        if not len(auth_token_arr) == 2:
            raise UnauthorizedException()

        if not auth_token_arr[0] == self.keyword:
            raise UnauthorizedException()

        token = token_manager.get({"token": auth_token_arr[1]})
        if not token:
            raise UnauthorizedException()

        user = token.user
        user.last_login = get_current_datetime()
        user.save()

        return user, token

    def authenticate_header(self, request):
        return self.keyword
