"""
Module providing serializers and OpenAPI examples for audit_logs endpoints.
"""

from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample
from utils.swagger import PaginationSerializer
from utils.swagger.common_swagger_functions import (
    get_list_success_example,
    get_by_id_success_example,
)


class AuditLogsDataSerializer(serializers.Serializer):
    """
    Serializer for audit logs data structure.
    """

    audit_id = serializers.CharField(
        help_text="Unique identifier for the audit log entry."
    )
    user_id = serializers.CharField(
        help_text="Unique identifier of the user who performed the action."
    )
    module_name = serializers.CharField(
        help_text="Name of the module where the action occurred."
    )
    http_method = serializers.CharField(
        help_text="HTTP method used in the request (GET, POST, etc.)."
    )
    request_path = serializers.CharField(help_text="Full path of the request URL.")
    client_ip = serializers.CharField(
        help_text="IP address of the client making the request."
    )
    client_user_agent = serializers.CharField(
        help_text="User agent string of the client."
    )
    request_route = serializers.CharField(help_text="Route used to access the API.")
    request_headers = serializers.JSONField(
        help_text="Headers included in the original request."
    )


class AuditLogsDataListSerializer(serializers.Serializer):
    """
    Serializer for the data list of audit logs.
    """

    list = AuditLogsDataSerializer(many=True, help_text="List of audit logs.")
    pagination = PaginationSerializer(
        help_text="Pagination information for the list of audit logs."
    )


class AuditLogsListResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of the audit logs list endpoint.
    """

    data = AuditLogsDataListSerializer(
        help_text="List of audit logs with pagination information."
    )
    errors = serializers.JSONField(
        help_text="Any errors for the response.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class AuditLogsResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of the audit logs list endpoint.
    """

    data = AuditLogsDataSerializer(help_text="Auditlogs information.")
    errors = serializers.JSONField(
        help_text="Any errors for the response.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


audit_log_ex_data = (
    {
        "audit_id": "e3744e32-8c42-468e-a11b-6595da3a12e1",
        "user_id": "70c2b240-27b1-4596-851b-95cb65f84842",
        "module_name": "audit_logs",
        "http_method": "GET",
        "request_path": "/api/audit-logs",
        "client_ip": "127.0.0.1",
        "request_route": "api/audit-logs",
        "client_user_agent": "PostmanRuntime/7.44.0",
        "request_headers": {
            "Content-Length": "10",
            "Content-Type": "text/plain",
            "User-Agent": "PostmanRuntime/7.44.0",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Postman-Token": "14406ac5-d700-4f76-be90-0316af10d742",
            "Host": "127.0.0.1:8000",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        },
    },
)
audit_get_by_id_success_example: OpenApiExample = get_by_id_success_example(
    name="Get Audit logs by Id - Success", data=audit_log_ex_data
)
audit_list_example_data = [audit_log_ex_data]
audit_list_success_example: OpenApiExample = get_list_success_example(
    name="List Audit - Success",
    list_data=audit_list_example_data,
)
