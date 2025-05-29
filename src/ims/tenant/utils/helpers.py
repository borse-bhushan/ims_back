"""
This module provides helper functions to manage customer tenant details
in thread local storage. It allows setting, getting, and clearing tenant and customer IDs
"""

import threading

_thread_locals = threading.local()


def set_tenant_details_to_request_thread(tenant_obj):
    """
    Set the tenant_id to the thread local storage.
    """
    _thread_locals.tenant_id = tenant_obj.tenant_id
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
