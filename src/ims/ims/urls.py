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
from utils.tenant_aware_path import add_to_tenant_aware_excluded_path_list

from .swagger import get_token_auth_schema, TenantAwareSchemaView

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
    # Stock Management API
    path(BASE_PATH, include("stock.urls")),
    # Notification Management API
    path(BASE_PATH, include("notification.urls")),
    # Supplier Management API
    path(BASE_PATH, include("supplier.urls")),
    # Reports Management API
    path(BASE_PATH, include("reports.urls")),
    # Audit Logs Management API
    path(BASE_PATH, include("audit_logs.urls")),
    # Monitoring API
    path(BASE_PATH, include("monitor.urls")),
    # Swagger Documentation
    path(
        add_to_tenant_aware_excluded_path_list(
            "api/schema", method_list=["GET"], add_base_path=False
        ),
        TenantAwareSchemaView.as_view(),
        name="schema",
    ),
    path(
        add_to_tenant_aware_excluded_path_list(
            "api/docs", method_list=["GET"], add_base_path=False
        ),
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        add_to_tenant_aware_excluded_path_list(
            "api/redoc", method_list=["GET"], add_base_path=False
        ),
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

handler404 = error_404
