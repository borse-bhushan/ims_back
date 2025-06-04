"""
Permission ViewSet for handling permission endpoints.
"""

from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from base.views import BaseView
from auth_user.constants import MethodEnum
from authentication import get_authentication_classes, register_permission

from utils.exceptions import codes
from utils.exceptions.exceptions import BadRequestError
from utils.messages import error
from utils.swagger import (
    responses_400,
    responses_404,
    responses_401,
    responses_400_example,
    responses_404_example,
    responses_401_example,
)

from ..db_access import permission_manager, role_permission_mapping_manager
from ..serializers import PermissionSerializer
from ..swagger import (
    PermissionResponseSerializer,
    PermissionListResponseSerializer,
    permission_create_success_example,
    permission_list_success_example,
    permission_get_by_id_success_example,
    permission_update_success_example,
    permission_delete_success_example,
)

MODULE = "Permission"


class PermissionViewSet(BaseView, viewsets.ViewSet):
    """
    ViewSet for handling permission endpoints.
    """

    is_pagination: bool = False
    manager = permission_manager
    lookup_field = "permission_id"
    serializer_class = PermissionSerializer

    get_authenticators = get_authentication_classes

    @extend_schema(
        responses={201: PermissionResponseSerializer, **responses_400, **responses_401},
        examples=[
            permission_create_success_example,
            responses_400_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.POST, f"Create {MODULE}")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

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
        return super().list_all(request, *args, **kwargs)

    @extend_schema(
        responses={200: PermissionResponseSerializer, **responses_404, **responses_401},
        examples=[
            permission_get_by_id_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={200: PermissionResponseSerializer, **responses_404, **responses_401},
        examples=[
            permission_update_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.PUT, f"Update {MODULE}")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def pre_delete(self, *_, **kwargs):
        """
        Checks if a permission can be deleted based on existing role-permission mappings.
        This method is called before deleting a permission to ensure the
        permission is not currently assigned to any role.
        """
        is_permission_already_mapped = role_permission_mapping_manager.exists(
            query={self.lookup_field: kwargs[self.lookup_field]}
        )

        if not is_permission_already_mapped:
            return True

        raise BadRequestError(message=error.ALREADY_IN_USED, code=codes.ALREADY_IN_USED)

    @extend_schema(
        responses={204: PermissionResponseSerializer, **responses_404, **responses_401},
        examples=[
            permission_delete_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.DELETE, f"Delete {MODULE}")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
