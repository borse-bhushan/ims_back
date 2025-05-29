"""
URL Configuration for project
"""

# Third Party Library Imports

from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


from utils.exceptions import error_404

from .swagger import get_token_auth_schema

get_token_auth_schema()

urlpatterns = [
    # Tenant Management API
    path("api/", include("tenant.urls")),
    # User Management API
    path("api/", include("auth_user.urls")),
    # Address Management API
    path("api/", include("address.urls")),
    # Audit Logs Management API
    path("api/", include("audit_logs.urls")),
    # Customer Management API
    path("api/", include("customer.urls")),
    # Monitoring API
    path("api/", include("monitor.urls")),
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
