"""
Tenant viewset for managing Tenants.
"""

from rest_framework import viewsets

from base.views.base import BaseView

from auth_user.constants import MethodEnum
from utils import functions as common_functions
from authentication import get_authentication_classes, register_permission


from .serializers import (
    TenantSerializer,
)
from .db_access import tenant_manager


MODULE = "Tenant"


class TenantViewSet(BaseView, viewsets.ViewSet):
    """
    ViewSet for managing tenant.
    """

    manager = tenant_manager
    lookup_field = "tenant_id"
    serializer_class = TenantSerializer
    authentication_classes = get_authentication_classes()

    def add_common_data(self, data, request, *args, **kwargs):
        """
        Adds common data to the request data.
        """

        user_id = request.user.user_id

        client_info = common_functions.get_client_info(request)

        data["created_by"] = user_id
        data["updated_by"] = user_id
        data["client_ip"] = client_info["client_ip"]
        data["client_user_agent"] = client_info["client_user_agent"]

        return data

    @register_permission(MODULE, MethodEnum.POST, f"Create {MODULE}")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @register_permission(MODULE, MethodEnum.PUT, f"Update {MODULE}")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @register_permission(MODULE, MethodEnum.DELETE, f"Delete {MODULE}")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
