"""
Serializer for user authentication.
"""

from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """

    username = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
