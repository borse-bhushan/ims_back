"""
This module adds the Performance time and System version in the response headers.
"""

from timeit import default_timer as timer

from django.utils import timezone

from utils.version import get_version_str


class AddResponseHeadersMiddleware:
    __doc__ = """
        This Middleware adds the Performance time and System version in the response headers.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        This method is called for each request.
        And it adds the Performance time and System version in the response headers.
        """
        start = timer()
        response = self.get_response(request)
        end = timer()

        _timedelta = timezone.timedelta(seconds=end - start)

        response["Version"] = get_version_str()
        response["Req-Performance-Time"] = str(_timedelta) + str(
            f"[HH:MM:SS:MS] | {_timedelta.total_seconds() * 1000}[MS]"
        )

        return response
