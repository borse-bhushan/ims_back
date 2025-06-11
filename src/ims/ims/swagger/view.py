"""
Custom Schema View for Multi-Tenant API Documentation.
"""

from drf_spectacular.utils import extend_schema
from drf_spectacular.views import SpectacularAPIView


class TenantAwareSchemaView(SpectacularAPIView):
    """
    A view that extends SpectacularAPIView to provide tenant-aware schema generation.
    This view ensures that the schema generation takes into account the current tenant
    context from the request. It overrides the get method to store the request object
    before generating the schema, allowing tenant-specific customizations.
    Inherits From:
    """

    @extend_schema(exclude=True)
    def get(self, request, *args, **kwargs):
        self.request = request
        return super().get(request, *args, **kwargs)
