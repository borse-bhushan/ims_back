"""
This file contains the response generator function which will be used to generate
the response in a consistent format.
"""

import typing

from rest_framework import status
from rest_framework.response import Response
from django.http.response import JsonResponse


class Empty:
    """
    This class is used to represent an empty value.
    """


def generate_response(
    data: typing.List | typing.Dict = None,
    status_code: int = status.HTTP_200_OK,
    messages: typing.List[typing.Dict] | typing.Dict = None,
    errors: typing.List[typing.Dict] | typing.Dict = None,
    success: bool | Empty = Empty,
    create_json_response: bool = False,
) -> Response | JsonResponse:
    """
    This function will generate the response in a consistent format
    :param data: The data to be sent in the response.
    :param status_code: The status code of the response.
    :param messages: The messages to be sent in the response.
    :param errors: The errors to be sent in the response.
    :param success: The success status of the response.
    :return: The response in a consistent format.
    """
    response: dict = {
        "data": data,
        "errors": errors,
        "messages": messages,
        "status_code": status_code,
    }

    is_success = None
    if success is not Empty:
        is_success = success

    elif errors:
        is_success = False

    else:
        is_success = True

    response["is_success"] = is_success

    if create_json_response:
        return JsonResponse(response, status=status_code)

    return Response(response, status=status_code)
