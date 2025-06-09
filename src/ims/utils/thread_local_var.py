"""
This module provides a thread-local variable that can be used to store data
"""

import threading

_local_variable = threading.local()


def get_thread_local_var():
    """
    Returns the thread-local variable instance.
    """
    return _local_variable
