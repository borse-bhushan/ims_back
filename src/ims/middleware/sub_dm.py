"""
Subdomain Middleware
This middleware extracts the subdomain from the request and attaches it to the request object.
"""

from rest_framework import status
from django.urls import resolve, Resolver404

from utils.messages import error
from utils.response import generate_response
from utils import functions as common_functions
from utils.tenant_aware_path import is_path_excluded_from_tenant_aware

from tenant.db_access import tenant_manager
from tenant.utils.helpers import (
    set_tenant_details_to_request_thread,
    clear_tenant_details_from_request_thread,
    set_request_tenant_aware,
    clear_request_tenant_aware,
)


class AttachSubdomainToRequestMiddleware:
    """
    Middleware to extract the subdomain from the request and attach it to the request object.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def get_tenant_details(self, request):
        sub_domain_data = common_functions.get_subdomain(request)

        if not sub_domain_data:
            return None

        tenant_obj = tenant_manager.cache.get(sub_domain_data)

        if not tenant_obj:
            tenant_obj = tenant_manager.disable_tenant_aware().get(
                query={"tenant_code": sub_domain_data}
            )
            tenant_manager.cache.set(sub_domain_data, tenant_obj)

        if not tenant_obj:
            return None

        return tenant_obj

    def __call__(self, request):
        """
        Process the request to extract the domain, subdomain and validate it against the database.
        If the domain, subdomain is valid, it will be attached to the request object.
        If the domain, subdomain is invalid, it will return a 400 Bad Request response
        with an error message.
        """

        tenant_obj = self.get_tenant_details(request=request)
        if tenant_obj:
            set_tenant_details_to_request_thread(tenant_obj)

        try:
            resolver_match = resolve(request.path)
            request.resolver_match = resolver_match
            route = resolver_match.route

            if is_path_excluded_from_tenant_aware(route, request.method.lower()):
                set_request_tenant_aware(is_tenant_aware=False)
                response = self.get_response(request)
                clear_request_tenant_aware()
                return response
        except Resolver404:
            pass

        if not tenant_obj:
            return generate_response(
                create_json_response=True,
                errors={"message": error.INVALID_TENANT},
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        set_request_tenant_aware()

        response = self.get_response(request)

        clear_request_tenant_aware()
        clear_tenant_details_from_request_thread()

        return response
