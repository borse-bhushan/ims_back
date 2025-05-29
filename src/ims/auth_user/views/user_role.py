"""
UserRole ViewSet for handling user-role endpoints.
"""

from rest_framework import viewsets, status
from drf_spectacular.utils import extend_schema

from utils.messages import success
from utils.swagger import (
    responses_400,
    responses_404,
    responses_401,
    responses_400_example,
    responses_404_example,
    responses_401_example,
)
from utils.response import generate_response
from utils.exceptions import NoDataFoundError

from auth_user.constants import MethodEnum
from base.views import CreateView, DeleteView, ListView
from authentication import get_authentication_classes, register_permission

from ..serializers import UserRoleSerializer, UserRoleListQuerySerializer
from ..db_access import user_role_mapping_manager, role_manager, user_manager
from ..swagger import (
    UserRoleResponseSerializer,
    UserRoleListResponseSerializer,
    user_role_create_success_example,
    user_role_list_success_example,
    user_role_delete_success_example,
)

MODULE = "UserRole"


class UserRoleViewSet(
    ListView,
    CreateView,
    DeleteView,
    viewsets.ViewSet,
):
    """
    ViewSet for handling user-role endpoints.
    """

    is_pagination: bool = False
    manager = user_role_mapping_manager
    serializer_class = UserRoleSerializer
    list_serializer_class = UserRoleListQuerySerializer
    authentication_classes = get_authentication_classes()

    @classmethod
    def get_method_view_mapping(cls, user_role_with_path_id=False):
        if user_role_with_path_id:
            return {
                **DeleteView.get_method_view_mapping(),
            }
        return {
            **ListView.get_method_view_mapping(),
            **CreateView.get_method_view_mapping(),
        }

    def get_list(self, objects, **_):
        role_ids = []
        user_ids = []
        for obj in objects:
            role_ids.append(obj.role_id)
            user_ids.append(obj.user_id)

        roles_map = role_manager.get_objects_mapping(
            query={"role_id__in": role_ids}, mapping_by="role_id"
        )
        users_map = user_manager.get_objects_mapping(
            query={"user_id__in": user_ids}, mapping_by="user_id"
        )

        data_list = []

        for obj in objects:
            data_dict = {}
            data_dict["role"] = roles_map[obj.role_id].to_dict()
            data_dict["user"] = users_map[obj.user_id].to_dict()
            data_list.append(data_dict)

        return data_list

    @extend_schema(
        responses={201: UserRoleResponseSerializer, **responses_400, **responses_401},
        examples=[
            user_role_create_success_example,
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
            200: UserRoleListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            user_role_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
        request=UserRoleListQuerySerializer,
    )
    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @extend_schema(
        responses={204: UserRoleResponseSerializer, **responses_404, **responses_401},
        examples=[
            user_role_delete_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.POST, f"Create {MODULE}")
    def destroy(self, request, **kwargs):
        """
        Deletes the user role mapping
        """
        query = {
            "user_id": kwargs["user_id"],
            "role_id": kwargs["role_id"],
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
