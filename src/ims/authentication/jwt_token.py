import jwt

from rest_framework.authentication import BaseAuthentication

from utils import settings
from auth_user.db_access import user_manager
from tenant.utils.helpers import is_request_tenant_aware

from .exception import UnauthorizedException


class JWTAuthentication(BaseAuthentication):
    keyword = "Bearer"

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith(f"{self.keyword} "):
            raise UnauthorizedException()

        token = auth_header.split(" ")[1]

        try:

            payload = jwt.decode(
                jwt=token,
                algorithms=["HS256"],
                options={"verify_exp": False},
                key=settings.read("SECRET_KEY"),
            )

        except (
            jwt.DecodeError,
            jwt.ExpiredSignatureError,
            jwt.ImmatureSignatureError,
            jwt.InvalidAlgorithmError,
            jwt.InvalidAudienceError,
            jwt.InvalidIssuedAtError,
            jwt.InvalidIssuerError,
            jwt.InvalidKeyError,
            jwt.InvalidSignatureError,
            jwt.InvalidTokenError,
            jwt.MissingRequiredClaimError,
            jwt.PyJWKClientConnectionError,
            jwt.PyJWKClientError,
            jwt.PyJWKError,
            jwt.PyJWKSetError,
            jwt.PyJWTError,
        ):

            raise UnauthorizedException()

        if is_request_tenant_aware():
            user = user_manager.cache.get(payload["user_id"])
            if user:
                return (user, None)

        user = user_manager.get({"user_id": payload["user_id"]})
        if not user:
            raise UnauthorizedException()

        user_manager.cache.set(payload["user_id"], user)

        return (user, None)

    def authenticate_header(self, request):
        return self.keyword
