"""
Audit logs serializers module.
"""

from .swagger import (
    AuditLogsListResponseSerializer,
    AuditLogsResponseSerializer,
    audit_list_success_example,
    audit_get_by_id_success_example,
)
__all__ = [
    "AuditLogsListResponseSerializer",
    "AuditLogsResponseSerializer",
    "audit_list_success_example",
    "audit_get_by_id_success_example",
]
