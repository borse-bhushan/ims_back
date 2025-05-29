"""
This file contains the common functions which are used in the project.
"""

import sys
import uuid

from urllib.parse import urlencode

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


def is_dev():
    """
    return true of the current env is DEV.
    """
    return is_env(constants.DEV)


def is_qa():
    """
    return true of the current env is QA.
    """
    return is_env(constants.QA)


def is_uat():
    """
    return true of the current env is UAT.
    """
    return is_env(constants.UAT)


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


def create_end_point(end_point: str):
    """
    Creates a complete endpoint URL by appending the given endpoint path to the base path.
    """

    if not end_point.startswith("/"):
        end_point = f"/{end_point}"

    return constants.BASE_PATH + end_point


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


def build_sso_redirect_url(
    sso_domain: str, sso_tenant_id: str, sso_path: str, query_params: dict
) -> str:
    """
    Builds the redirect URL for Microsoft SSO OAuth2.

    Args:
        config (dict): Configuration dictionary containing required keys.

    Returns:
        str: The full redirect URL.
    """

    base_url = create_url(create_url(sso_domain, sso_tenant_id), sso_path)

    return f"{base_url}?{urlencode(query_params)}"


def create_url(host: str, path: str):
    """
    This will help to create the URL  [https://<host>/<path>].
    """
    if not host:
        return None

    if not host.endswith("/"):
        host += "/"

    if path.startswith("/"):
        path = path.removeprefix("/")

    return f"{host}{path}"
