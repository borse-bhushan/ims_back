"""
Permission ViewSet for handling permission endpoints.
"""

from rest_framework import viewsets
from drf_spectacular.utils import extend_schema


from base.views import CreateView, ListView
from authentication import (
    get_authentication_classes,
    register_permission,
    get_default_authentication_class,
)


from utils.swagger import (
    responses_404,
    responses_401,
    responses_404_example,
    responses_401_example,
    responses_400,
    SuccessResponseSerializer,
)

from tenant.utils.tenant_conf import get_tenant_db_name


from auth_user.constants import MethodEnum
from auth_user.db_access import permission_manager
from auth_user.utils.permission import load_permission
from auth_user.serializers import PermissionListQuerySerializer
from auth_user.swagger import (
    PermissionListResponseSerializer,
    permission_list_success_example,
    permission_create_success_example,
)

MODULE = "Permission"


class ListCreatePermissionViewSet(
    ListView,
    CreateView,
    viewsets.ViewSet,
):
    """
    Load the permission array against the tenant.
    """

    is_pagination: bool = False
    manager = permission_manager
    is_common_data_needed = False
    serializer_class = PermissionListQuerySerializer
    list_serializer_class = PermissionListQuerySerializer
    get_authenticators = get_default_authentication_class
    filter_fields = ["tenant_id"]

    @classmethod
    def get_method_view_mapping(cls):
        return {
            **ListView.get_method_view_mapping(),
            **CreateView.get_method_view_mapping(),
        }

    def using(self, request, **kwargs):
        qp = request.query_params.dict()
        return get_tenant_db_name(qp["tenant_id"])

    @extend_schema(
        request={},
        responses={
            201: SuccessResponseSerializer,
            **responses_404,
            **responses_401,
            **responses_400,
        },
        examples=[
            responses_404_example,
            responses_401_example,
            permission_create_success_example,
        ],
        tags=[MODULE],
    )
    @register_permission(
        MODULE, MethodEnum.POST, f"Create {MODULE}", create_permission=False
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def save(self, data, **kwargs):
        load_permission.load_permissions_for_tenant(
            request=kwargs["request"],
            tenant_id=data["tenant_id"],
        )
        return None

    @extend_schema(
        responses={
            200: PermissionListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            permission_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
        parameters=[PermissionListQuerySerializer],
    )
    @register_permission(
        MODULE, MethodEnum.GET, f"Get {MODULE}", create_permission=False
    )
    def list_all(self, request, *args, **kwargs):
        """Get the list of permissions and modules"""
        return super().list_all(request, *args, **kwargs)


class PermissionViewSet(ListView, viewsets.ViewSet):
    """
    ViewSet for handling permission endpoints.
    """

    get_authenticators = get_authentication_classes

    is_pagination: bool = False
    manager = permission_manager

    @extend_schema(
        responses={
            200: PermissionListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            permission_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def list_all(self, request, *args, **kwargs):
        """Get the list of permissions and modules"""
        return super().list_all(request, *args, **kwargs)
