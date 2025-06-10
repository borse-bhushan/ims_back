"""
User ViewSet for handling user endpoints.
"""

from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from auth_user.constants import MethodEnum
from base.views import BaseView, RetrieveView, CreateView, ListView
from authentication import get_authentication_classes, register_permission

from utils.response import generate_response
from utils.swagger import (
    responses_400,
    responses_404,
    responses_401,
    responses_400_example,
    responses_404_example,
    responses_401_example,
)

from ..db_access import user_manager
from ..serializers import (
    UserSerializer,
    UserCompanyAdminListQuerySerializer,
    UserCompanyAdminSerializer,
)
from ..swagger import (
    UserResponseSerializer,
    UserListResponseSerializer,
    user_create_success_example,
    user_list_success_example,
    user_get_by_id_success_example,
    user_update_success_example,
    user_delete_success_example,
)

MODULE = "User"
MODULE_PROFILE = "User Profile"


class UserViewSetBase:

    def save(self, data, **kwargs):
        """
        Save password in hash
        """

        user_obj = super().save(data, **kwargs)
        user_obj.set_password(user_obj.password)
        user_obj.save()

        return user_obj

    @extend_schema(
        responses={201: UserResponseSerializer, **responses_400, **responses_401},
        examples=[
            user_create_success_example,
            responses_400_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.POST, f"Create {MODULE}")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        responses={200: UserListResponseSerializer, **responses_404, **responses_401},
        examples=[
            user_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @extend_schema(
        responses={200: UserResponseSerializer, **responses_404, **responses_401},
        examples=[
            user_get_by_id_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={200: UserResponseSerializer, **responses_404, **responses_401},
        examples=[
            user_update_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.PUT, f"Update {MODULE}")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        responses={204: UserResponseSerializer, **responses_404, **responses_401},
        examples=[
            user_delete_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.DELETE, f"Delete {MODULE}")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class UserViewSet(UserViewSetBase, BaseView, viewsets.ViewSet):
    """
    ViewSet for handling user endpoints.
    """

    manager = user_manager
    lookup_field = "user_id"
    serializer_class = UserSerializer

    get_authenticators = get_authentication_classes


class UserCompanyAdminsViewSet(
    UserViewSetBase,
    ListView,
    CreateView,
    viewsets.ViewSet,
):
    """
    ViewSet for handling user endpoints.
    """

    manager = user_manager
    lookup_field = "user_id"
    serializer_class = UserCompanyAdminSerializer
    list_serializer_class = UserCompanyAdminListQuerySerializer

    filter_fields = ["tenant_id"]

    get_authenticators = get_authentication_classes

    @classmethod
    def get_method_view_mapping(cls):
        """
        Get the mapping of http method and view method
        """
        return {
            **CreateView.get_method_view_mapping(),
            **ListView.get_method_view_mapping(),
        }


class UserProfileViewSet(RetrieveView, viewsets.ViewSet):
    """
    ViewSet for handling user profile endpoints.
    """

    get_authenticators = get_authentication_classes

    @register_permission(
        MODULE_PROFILE,
        MethodEnum.POST,
        f"Get {MODULE_PROFILE}",
        check=False,
    )
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve the user profile information.
        """
        return generate_response(data={**request.user.to_dict()})
