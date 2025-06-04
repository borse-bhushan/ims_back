"""
URL Configuration for project
"""

from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


from utils.constants import BASE_PATH
from utils.exceptions import error_404

from .swagger import get_token_auth_schema

get_token_auth_schema()


urlpatterns = [
    # Tenant Management API
    path(BASE_PATH, include("tenant.urls")),
    # User Management API
    path(BASE_PATH, include("auth_user.urls")),
    # Category Management API
    path(BASE_PATH, include("category.urls")),
    # Product Management API
    path(BASE_PATH, include("product.urls")),
    # Supplier Management API
    path(BASE_PATH, include("supplier.urls")),
    # Audit Logs Management API
    path(BASE_PATH, include("audit_logs.urls")),
    # Monitoring API
    path(BASE_PATH, include("monitor.urls")),
    # Swagger Documentation
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/redoc", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

handler404 = error_404
