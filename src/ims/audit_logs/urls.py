"""
AuditLogs URL routing module.
"""

from django.urls import path
from .views import AuditLogViewSet


urlpatterns = [
    path(
        "audit-logs",
        AuditLogViewSet.as_view(AuditLogViewSet.get_method_view_mapping()),
        name="audit-logs",
    ),
    path(
        "audit-logs/<str:audit_id>",
        AuditLogViewSet.as_view(AuditLogViewSet.get_method_view_mapping(True)),
        name="audit-log",
    ),
]
