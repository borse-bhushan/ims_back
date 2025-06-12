"""
Filters API endpoints shown in the schema based on the request host.
"""

from utils.tenant_aware_path import is_path_excluded_from_tenant_aware
from tenant.utils.helpers import get_tenant_details_from_request_thread


def domain_based_preprocessing_hook(endpoints, **kwargs):
    """
    Filters API endpoints shown in the schema based on the request host.
    """

    is_tenant_aware_req = get_tenant_details_from_request_thread(
        raise_err=False,
    )["tenant_id"]

    filtered = []
    for path, path_regex, method, callback in endpoints:

        if is_tenant_aware_req:
            if not is_path_excluded_from_tenant_aware(path_regex, method):
                filtered.append((path, path_regex, method, callback))
        else:
            if is_path_excluded_from_tenant_aware(path_regex, method):
                filtered.append((path, path_regex, method, callback))

    return filtered
