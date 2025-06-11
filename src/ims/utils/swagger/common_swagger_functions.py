"""This file is for the comman data passing"""

from rest_framework import status
from drf_spectacular.utils import OpenApiExample

from utils.messages import success


def get_delete_success_example(
    name: str = "Delete - Success", message=success.DELETED_SUCCESSFULLY
):
    """return success message after delete data"""
    return OpenApiExample(
        name=name,
        value={
            "data": None,
            "errors": None,
            "messages": {"message": message} if message else None,
            "status_code": status.HTTP_204_NO_CONTENT,
            "is_success": True,
        },
        response_only=True,
        status_codes=[str(status.HTTP_204_NO_CONTENT)],
    )


def get_update_success_example(
    name: str = "Update - Success", data=None, message=success.UPDATED_SUCCESSFULLY
):
    """Return OpenAPI  update success response."""
    return OpenApiExample(
        name=name,
        value={
            "data": data,
            "errors": None,
            "messages": {"message": message} if message else None,
            "status_code": status.HTTP_200_OK,
            "is_success": True,
        },
        response_only=True,
        status_codes=[str(status.HTTP_200_OK)],
    )


def get_create_success_example(
    name: str = "Create - Success", data=None, message=success.CREATED_SUCCESSFULLY
):
    """Return OpenAPI  create success response."""
    return OpenApiExample(
        name=name,
        value={
            "data": data,
            "errors": None,
            "messages": {"message": message} if message else None,
            "status_code": status.HTTP_201_CREATED,
            "is_success": True,
        },
        response_only=True,
        status_codes=[str(status.HTTP_201_CREATED)],
    )


def get_list_success_example(
    name: str = "List - Success",
    list_data=None,
    pagination_data=True,
    message=None,
    status_code: int = status.HTTP_200_OK,
):
    """Return OpenAPI success response for list endpoints."""

    _pagination_data = {
        "count": 1,
        "page_size": 1,
        "current_page": 1,
        "total_pages": 1,
    }

    if pagination_data:
        if not isinstance(pagination_data, bool):
            _pagination_data = pagination_data

    data = {}

    if pagination_data:
        data["list"] = list_data
        data["pagination"] = _pagination_data
    else:
        data = list_data

    return OpenApiExample(
        name=name,
        value={
            "data": data,
            "errors": None,
            "messages": message,
            "status_code": status_code,
            "is_success": True,
        },
        response_only=True,
        status_codes=[str(status_code)],
    )


def get_by_id_success_example(
    name: str = "Get Data - Success",
    data=None,
    message=None,
    status_code: int = status.HTTP_200_OK,
):
    """Return OpenAPI success response for data by id endpoints."""
    return OpenApiExample(
        name=name,
        value={
            "data": data,
            "errors": None,
            "messages": {message: message} if message else None,
            "status_code": status_code,
            "is_success": True,
        },
        response_only=True,
        status_codes=[str(status_code)],
    )
