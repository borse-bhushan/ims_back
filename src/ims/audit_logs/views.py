"""
Audit logs ViewSet
This module contains the AuditLogViewSet class, which provides
CRUD operations for managing audit logs.
"""

from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from base.views.base import RetrieveView, ListView
from auth_user.constants import MethodEnum
from authentication import get_authentication_classes, register_permission
from utils.swagger import (
    responses_404,
    responses_401,
    responses_404_example,
    responses_401_example,
)
from .serializers import (
    AuditLogsListResponseSerializer,
    audit_get_by_id_success_example,
    audit_list_success_example,
    AuditLogsResponseSerializer,
)
from .db_access import audit_logs_manager


MODULE_NAME = "Audit Logs"


class AuditLogViewSet(RetrieveView, ListView, viewsets.ViewSet):
    """
    ViewSet for managing AuditLog objects.
    """

    manager = audit_logs_manager
    lookup_field = "audit_id"

    get_authenticators = get_authentication_classes

    @classmethod
    def get_method_view_mapping(cls, with_path_id=False):
        if with_path_id:
            return {
                **RetrieveView.get_method_view_mapping(),
            }
        return {
            **ListView.get_method_view_mapping(),
        }

    @extend_schema(
        responses={
            200: AuditLogsListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            audit_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE_NAME],
    )
    @register_permission(MODULE_NAME, MethodEnum.GET, f"List {MODULE_NAME}")
    def list_all(self, request, *args, **kwargs):
        """
        Retrieve a list of all AuditLog records.
        """
        return super().list_all(request, *args, **kwargs)

    @extend_schema(
        responses={200: AuditLogsResponseSerializer, **responses_404, **responses_401},
        examples=[
            audit_get_by_id_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE_NAME],
    )
    @register_permission(MODULE_NAME, MethodEnum.GET, f"Get {MODULE_NAME}")
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a single AuditLog record by ID.
        """
        return super().retrieve(request, *args, **kwargs)
