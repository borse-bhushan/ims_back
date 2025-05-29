"""
Subdomain Middleware
This middleware extracts the subdomain from the request and attaches it to the request object.
"""

from rest_framework import status

from utils.messages import error
from utils.response import generate_response
from customer.db_access import customer_sso_info_manager
from customer.helpers import (
    set_customer_tenant_details_to_request_thread,
    clear_customer_tenant_details_from_request_thread,
)


class AttachSubdomainToRequestMiddleware:
    """
    Middleware to extract the subdomain from the request and attach it to the request object.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Process the request to extract the domain, subdomain and validate it against the database.
        If the domain, subdomain is valid, it will be attached to the request object.
        If the domain, subdomain is invalid, it will return a 400 Bad Request response
        with an error message.
        """
        domain_data = self.get_subdomain(request)
        customer_sso_info_manager.disable_tenant_aware()
        customer_sso_info_obj = customer_sso_info_manager.get(query=domain_data)
        customer_sso_info_manager.enable_tenant_aware()

        if not customer_sso_info_obj:
            return generate_response(
                create_json_response=True,
                errors={"message": error.INVALID_DOMAIN},
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        set_customer_tenant_details_to_request_thread(customer_sso_info_obj)

        response = self.get_response(request)

        clear_customer_tenant_details_from_request_thread()

        return response

    def get_subdomain(self, request):
        """
        Extract the subdomain from the request host.
        If the host is localhost, return None.
        If the host has more than two parts, return the first part as the
        subdomain and second as domain.
        """
        host = request.get_host().split(":")[0]

        data_dict = {}

        if host == "127.0.0.1":
            data_dict["customer_domain"] = host
            data_dict["customer_sub_domain"] = None
            return data_dict

        parts = host.split(".")
        if len(parts) > 2:
            data_dict["customer_domain"] = parts[1]
            data_dict["customer_sub_domain"] = parts[0]
            return data_dict

        data_dict["customer_domain"] = parts[0]
        data_dict["customer_sub_domain"] = None

        return data_dict
