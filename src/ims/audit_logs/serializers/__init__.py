"""
Audit logs serializers module.
"""

from .swagger import (
    AuditLogsListResponseSerializer,
    AuditLogsResponseSerializer,
    audit_list_success_example,
    audit_getById_success_example,
)
__all__ = [
    "AuditLogsListResponseSerializer",
    "AuditLogsResponseSerializer",
    "audit_list_success_example",
    "audit_getById_success_example",
]
