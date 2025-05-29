"""
Role ViewSet for handling role endpoints.
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

from ..db_access import role_manager, user_role_mapping_manager
from ..serializers import RoleSerializer
from ..swagger import (
    RoleResponseSerializer,
    RoleListResponseSerializer,
    role_create_success_example,
    role_list_success_example,
    role_get_by_id_success_example,
    role_update_success_example,
    role_delete_success_example,
)

MODULE = "Role"


class RoleViewSet(BaseView, viewsets.ViewSet):
    """
    ViewSet for handling role endpoints.
    """

    authentication_classes = get_authentication_classes()
    manager = role_manager
    serializer_class = RoleSerializer
    lookup_field = "role_id"

    @extend_schema(
        responses={201: RoleResponseSerializer, **responses_400, **responses_401},
        examples=[
            role_create_success_example,
            responses_400_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.POST, f"Create {MODULE}")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        responses={200: RoleListResponseSerializer, **responses_404, **responses_401},
        examples=[
            role_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @extend_schema(
        responses={200: RoleResponseSerializer, **responses_404, **responses_401},
        examples=[
            role_get_by_id_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={200: RoleResponseSerializer, **responses_404, **responses_401},
        examples=[
            role_update_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.POST, f"Create {MODULE}")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def pre_delete(self, *_, **kwargs):
        """
        Checks if a role can be deleted based on existing user-role mappings.
        This method is called before deleting a role to ensure the
        role is not currently assigned to any users.
        Returns:
            bool: True if the role can be deleted (not mapped to any users)
        Raises:
            BadRequestError: If the role is already mapped to one or more users
        Example:
            When attempting to delete a role that is assigned to users:
            >>> pre_delete(role_id=123)
            BadRequestError: Role is already in use
        """
        is_role_already_mapped = user_role_mapping_manager.exists(
            query={self.lookup_field: kwargs[self.lookup_field]}
        )

        if not is_role_already_mapped:
            return True

        raise BadRequestError(message=error.ALREADY_IN_USED, code=codes.ALREADY_IN_USED)

    @extend_schema(
        responses={204: RoleResponseSerializer, **responses_404, **responses_401},
        examples=[
            role_delete_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.DELETE, f"Delete {MODULE}")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
