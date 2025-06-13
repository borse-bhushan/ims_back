"""
Login and Logout ViewSets for handling user authentication.
"""

import jwt
import secrets

from rest_framework import status, viewsets
from drf_spectacular.utils import extend_schema

from base.views import CreateView, DeleteView

from auth_user.constants import MethodEnum

from authentication.exception import WrongCredentialsException
from authentication import get_authentication_classes, register_permission

from audit_logs.utils.audit_log import create_audit_log_entry

from tenant.constants import AuthenticationTypeEnum
from tenant.utils.helpers import is_request_tenant_aware
from tenant.db_access import tenant_configuration_manager

from utils.messages import success, error
from utils.response.response import generate_response
from utils import functions as common_functions, settings
from utils.exceptions import BadRequestError, ValidationError
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

    def check_password(self, username, password, request):
        """
        Check if the provided password is correct for the given username.
        """

        query = {"email": username}
        if not is_request_tenant_aware():
            query["role_id"] = RoleEnum.SUPER_ADMIN

        user_obj = user_manager.get(query=query)

        if not user_obj:
            raise WrongCredentialsException()

        if not user_obj.check_password(password):
            raise WrongCredentialsException()

        user_obj.last_login = common_functions.get_current_datetime()
        user_obj.save(update_fields=["last_login"])

        request.user = user_obj

        create_audit_log_entry(
            request=request,
            action=request.method,
            module_name=MODULE_NAME,
        )

        return user_obj

    def pre_save(self, data: dict, **kwargs):
        """
        Handle user login by validating credentials and generating a token.
        """

        request = kwargs["request"]
        user_obj = self.check_password(data["username"], data["password"], request)

        self.manager.delete({"user": user_obj}, soft_delete=False)

        return {"user": user_obj, "token": secrets.token_hex(16).upper()}

    def post_save(self, obj, **kwargs):
        """
        Handle post-save actions after user login.
        """

        if is_request_tenant_aware():
            user_manager.cache.set(obj.user_id, obj.user)

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

        if is_request_tenant_aware():

            tenant_config_obj = tenant_configuration_manager.get({})

            if not tenant_config_obj:
                raise BadRequestError(error.TENANT_CONFIGURATION_NOT_FOUND)

            at = tenant_config_obj.authentication_type

            if not at:
                raise BadRequestError(error.AUTHENTICATION_NOT_CONFIGURED)

            if at == AuthenticationTypeEnum.JWT_TOKEN:
                return self.jwt_login(request, *args, **kwargs)

        return super().create(request, *args, **kwargs)

    def jwt_login(self, request, *args, **kwargs):
        """
        Handle JWT login for the user.
        This method is used to authenticate the user and generate a JWT token.
        """

        serializer_obj = self.serializer_class(data=request.data)

        is_valid = serializer_obj.is_valid()

        if not is_valid:
            raise ValidationError(serializer_obj.errors)

        data = serializer_obj.validated_data

        user_obj = self.check_password(data["username"], data["password"], request)

        access_token = jwt.encode(
            algorithm="HS256",
            key=settings.read("SECRET_KEY"),
            payload={"user_id": user_obj.user_id},
        )

        if is_request_tenant_aware():
            user_manager.cache.set(user_obj.user_id, user_obj)

        return generate_response(
            data={"token": access_token, "created_dtm": user_obj.last_login},
            status_code=status.HTTP_201_CREATED,
            messages={"message": success.LOGIN_SUCCESSFULLY},
        )


class LogoutViewSet(DeleteView, viewsets.ViewSet):
    """
    ViewSet for handling logout related endpoints.
    """

    manager = token_manager
    get_authenticators = get_authentication_classes

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
