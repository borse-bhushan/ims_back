"""This file is for the comman data passing"""

from drf_spectacular.utils import OpenApiExample
from utils.messages import success


def get_delete_success_example(name: str = "Delete - Success", message=None):
    """return success message after delete data"""
    return OpenApiExample(
        name=name,
        value={
            "data": None,
            "errors": None,
            "messages": message or success.DELETED_SUCCESSFULLY,
            "status_code": 204,
            "is_success": True,
        },
        response_only=True,
        status_codes=["204"],
    )


def get_update_success_example(name: str = "Update - Success", data=None, message=None):
    """Return OpenAPI  update success response."""
    return OpenApiExample(
        name=name,
        value={
            "data": data,
            "errors": None,
            "messages": message or success.UPDATED_SUCCESSFULLY,
            "status_code": 200,
            "is_success": True,
        },
        response_only=True,
        status_codes=["200"],
    )


def get_create_success_example(name: str = "Create - Success", data=None, message=None):
    """Return OpenAPI  create success response."""
    return OpenApiExample(
        name=name,
        value={
            "data": data,
            "errors": None,
            "messages": message or success.CREATED_SUCCESSFULLY,
            "status_code": 201,
            "is_success": True,
        },
        response_only=True,
        status_codes=["201"],
    )


def get_list_success_example(
    name: str = "List - Success",
    list_data=None,
    pagination_data=None,
    message=None,
    status_code: int = 200,
):
    """Return OpenAPI success response for list endpoints."""
    return OpenApiExample(
        name=name,
        value={
            "data": {
                "list": list_data or [],
                "pagination": pagination_data
                or {
                    "count": 0,
                    "page_size": 10,
                    "current_page": 1,
                    "total_pages": 1,
                },
            },
            "errors": None,
            "messages": message,
            "status_code": status_code,
            "is_success": True,
        },
        response_only=True,
        status_codes=[str(status_code)],
    )


def get_by_id_success_example(
    name: str = "Get Data - Success", data=None, message=None, status_code: int = 200
):
    """Return OpenAPI success response for data by id endpoints."""
    return OpenApiExample(
        name=name,
        value={
            "data": data,
            "errors": None,
            "messages": message,
            "status_code": 200,
            "is_success": True,
        },
        response_only=True,
        status_codes=[str(status_code)],
    )
