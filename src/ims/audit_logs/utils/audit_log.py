"""
Create an audit log entry for actions performed in the application.
"""

from utils.functions import get_client_info

from ..db_access import audit_logs_manager


def create_audit_log_entry(request, module_name, action):
    """
    Create an audit log entry with the provided request and module name.
    """
    user_id = request.user.user_id
    client_info = get_client_info(request)
    headers = dict(request.headers) if hasattr(request, "headers") else {}
    headers.pop("Authorization", None)  # Remove Authorization header if present

    data = {
        "user_id": user_id,
        "created_by": user_id,
        "updated_by": user_id,
        "http_method": action,
        "module_name": module_name,
        "request_headers": headers,
        "request_path": request.path,
        "client_ip": client_info["client_ip"],
        "request_route": request.resolver_match.route,
        "client_user_agent": client_info["client_user_agent"],
    }
    return audit_logs_manager.create(data=data)
