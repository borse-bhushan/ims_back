"""
This module provides helper functions to manage customer tenant details
in thread local storage. It allows setting, getting, and clearing tenant and customer IDs
"""

from utils.thread_local_var import get_thread_local_var


_thread_locals = get_thread_local_var()


def set_tenant_details_to_request_thread(tenant_obj):
    """
    Set the tenant_id to the thread local storage.
    """
    _thread_locals.tenant_id = getattr(tenant_obj, "tenant_id", None)
    return True


def get_tenant_details_from_request_thread():
    """
    Get the tenant_id from the thread local storage.
    """

    return {
        "tenant_id": _thread_locals.tenant_id,
    }


def clear_tenant_details_from_request_thread():
    """
    Clear the tenant_id from the thread local storage.
    """
    del _thread_locals.tenant_id
    return True


def set_request_tenant_aware(is_tenant_aware=True):
    """
    Set the tenant-aware status for the request.

    Args:
        is_tenant_aware (bool): True if tenant-aware, False otherwise.
    """

    _thread_locals.is_tenant_aware = is_tenant_aware
    return True


def is_request_tenant_aware():
    """
    Check if the request is tenant-aware.

    Returns:
        bool: True if tenant-aware, False otherwise.
    """
    return getattr(_thread_locals, "is_tenant_aware", True)


def clear_request_tenant_aware():
    """
    Clear the tenant-aware status for the request.
    """
    del _thread_locals.is_tenant_aware
    return True
