"""
ViewSet for handling role-permission endpoints.
"""

from rest_framework import viewsets, status
from drf_spectacular.utils import extend_schema

from utils.swagger import (
    responses_400,
    responses_404,
    responses_401,
    responses_400_example,
    responses_404_example,
    responses_401_example,
    SuccessResponseSerializer,
)
from utils.messages import success
from utils.response import generate_response
from utils.exceptions import NoDataFoundError
from auth_user.constants import MethodEnum
from base.views import CreateView, DeleteView, ListView
from authentication import get_authentication_classes, register_permission


from ..serializers import RolePermissionSerializer
from ..db_access import role_permission_mapping_manager
from ..swagger import (
    RolePermissionResponseSerializer,
    RolePermissionListResponseSerializer,
    role_permission_create_example,
    role_permission_list_example,
    role_permission_delete_example,
)

MODULE = "Role Permission"


class RolePermissionViewSet(CreateView, DeleteView, ListView, viewsets.ViewSet):
    """
    ViewSet for handling role-permission endpoints.
    """

    many = True
    is_pagination: bool = False
    manager = role_permission_mapping_manager
    serializer_class = RolePermissionSerializer

    get_authenticators = get_authentication_classes

    @classmethod
    def get_method_view_mapping(cls, with_path_id=False):
        if with_path_id:
            return {
                **DeleteView.get_method_view_mapping(),
            }
        return {
            **ListView.get_method_view_mapping(),
            **CreateView.get_method_view_mapping(),
        }

    @extend_schema(
        request=RolePermissionSerializer(many=True),
        responses={
            201: RolePermissionResponseSerializer,
            **responses_400,
            **responses_401,
        },
        examples=[
            role_permission_create_example,
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
            200: RolePermissionListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            role_permission_list_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @extend_schema(
        responses={204: SuccessResponseSerializer, **responses_404, **responses_401},
        examples=[
            role_permission_delete_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.POST, f"Create {MODULE}")
    def destroy(self, request, **kwargs):
        """
        Deletes the role-permission mapping
        """
        query = {
            "role_id": kwargs["role_id"],
            "permission_id": kwargs["permission_id"],
        }

        obj = self.manager.get(query=query)
        if not obj:
            raise NoDataFoundError()

        self.manager.delete(query=query)

        return generate_response(
            data=None,
            messages={"message": success.DELETED_SUCCESSFULLY},
            status_code=status.HTTP_204_NO_CONTENT,
        )
