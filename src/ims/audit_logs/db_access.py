"""
audit_logs manager module.
This module contains the auditLogsManager class, which is responsible for managing
the AuditLogs model.
It provides methods for retrieving audit log records.
"""

from base.db_access import manager
from .models import AuditLogs


class AuditLogsManager(manager.Manager[AuditLogs]):
    """
    Manager class for the AuditLogs model.
    """

    model = AuditLogs


audit_logs_manager = AuditLogsManager()
