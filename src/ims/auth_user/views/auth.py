"""
Login and Logout ViewSets for handling user authentication.
"""

import secrets


from rest_framework import status, viewsets
from drf_spectacular.utils import extend_schema

from base.views import CreateView, DeleteView

from auth_user.constants import MethodEnum

from authentication.exception import WrongCredentialsException
from authentication import get_authentication_classes, register_permission

from audit_logs.helpers import create_audit_log_entry

from tenant.utils.helpers import is_request_tenant_aware

from utils.messages import success
from utils import functions as common_functions
from utils.response.response import generate_response
from utils.swagger import (
    responses_400,
    responses_401,
    responses_400_example,
)


from ..constants import RoleEnum
from ..serializers import LoginSerializer
from ..db_access import token_manager, user_manager
from ..serializers.swagger import (
    LoginResponseSerializer,
    LogoutResponseSerializer,
    login_success_example,
    logout_success_example,
    responses_401_example,
)

MODULE_NAME = "Authentication"


class LoginViewSet(CreateView, viewsets.ViewSet):
    """
    ViewSet for handling login endpoints.
    """

    manager = token_manager
    authentication_classes = []
    is_common_data_needed = False
    serializer_class = LoginSerializer

    def pre_save(self, data: dict, **kwargs):
        """
        Handle user login by validating credentials and generating a token.
        """

        query = {"email": data["username"], "password": data["password"]}

        if not is_request_tenant_aware():
            query["role_id"] = RoleEnum.SUPER_ADMIN

        user_obj = user_manager.get(query=query)

        if not user_obj:
            raise WrongCredentialsException()

        self.manager.delete({"user": user_obj}, soft_delete=False)

        request = kwargs["request"]
        request.user = user_obj
        common_info = common_functions.get_client_info(request)

        create_audit_log_entry(
            request=request,
            action=request.method,
            module_name=MODULE_NAME,
        )

        return {"user": user_obj, "token": secrets.token_hex(16).upper(), **common_info}

    def post_save(self, obj, **kwargs):
        """
        Handle post-save actions after user login.
        """

        return generate_response(
            data=obj.to_dict(),
            status_code=status.HTTP_201_CREATED,
            messages={"message": success.LOGIN_SUCCESSFULLY},
        )

    @extend_schema(
        request=LoginSerializer,
        responses={201: LoginResponseSerializer, **responses_401, **responses_400},
        examples=[login_success_example, responses_401_example, responses_400_example],
        tags=[MODULE_NAME],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class LogoutViewSet(DeleteView, viewsets.ViewSet):
    """
    ViewSet for handling logout related endpoints.
    """

    manager = token_manager

    authentication_classes = get_authentication_classes()

    @extend_schema(
        request=LogoutResponseSerializer,
        responses={204: LogoutResponseSerializer, **responses_401},
        examples=[logout_success_example, responses_401_example],
        tags=[MODULE_NAME],
    )
    @register_permission(MODULE_NAME, MethodEnum.DELETE, "Logout", check=False)
    def destroy(self, request, **kwargs):
        """
        Handle user logout by deleting the token associated with the user.
        """

        self.manager.delete({"user": request.user}, soft_delete=False)

        return generate_response(
            data=None,
            status_code=status.HTTP_204_NO_CONTENT,
            messages={"message": success.LOGOUT_SUCCESSFULLY},
        )
