from utils.thread_local_var import get_thread_local_var


_local_thread_var = get_thread_local_var()


def set_audit_log_id(audit_log_id):
    """
    Set the audit log ID in the thread-local storage.
    """
    _local_thread_var.audit_log_id = audit_log_id


def get_audit_log_id():
    """
    Get the audit log ID from the thread-local storage.
    """
    return getattr(_local_thread_var, "audit_log_id", None)


def clear_audit_log_id():
    """
    Clear the audit log ID from the thread-local storage.
    """
    del _local_thread_var.audit_log_id
    return True
