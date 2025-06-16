"""
This file contains the common functions which are used in the project.
"""

import sys
import uuid

from django.utils import timezone

from utils import constants, settings


def get_uuid():
    """
    It's used to generate the UUID.
    """
    return str(uuid.uuid4())


def is_env(env: str):
    """
    Check if the current env is given env or not.
    """
    return env == c_env()


def is_local():
    """
    return true of the current env is LOCAL.
    """
    return is_env(constants.LOCAL)


def is_prod():
    """
    return true of the current env is PROD.
    """
    return is_env(constants.PROD)


# current env
def c_env():
    """
    Return the env which app is running.
    """
    return settings.read("ENV").upper()


def is_linux():
    """
    Check if the app is running on linux or not.
    """
    return "linux" in sys.platform


def get_current_datetime():
    """
    Return the current datetime. With system timezone.
    """
    return timezone.now()


def get_client_info(request):
    """
    Get the real client IP address, supporting proxies and Docker.
    Get the user agent from the request headers.
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")

    user_agent = request.META.get("HTTP_USER_AGENT", "")

    return {"client_ip": ip, "client_user_agent": user_agent}


def get_subdomain(request):
    """
    Extract the subdomain from the request host.
    """
    host = request.get_host().split(":")[0]

    parts = host.split(".")
    if len(parts) >= 2:
        return parts[0]

    return None


def create_stock_reference(prefix: str, length: int = 8):
    """
    Create a unique stock reference with the given prefix and length.
    The code will be a combination of the prefix and a random UUID.
    """

    unique_part = uuid.uuid4().hex[:length]
    return f"{prefix}:{unique_part}".upper()
