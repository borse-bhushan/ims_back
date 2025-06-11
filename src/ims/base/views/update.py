"""
This module contains the BasePatchView class, which provides a base implementation
for updating objects based on query parameters. It raises a 404 error if the object is not found.
"""

from rest_framework import serializers, status

from ..constants import PATCH, PUT

from base.db_access import Manager
from utils.messages import error, success
from utils.response import generate_response
from utils.exceptions import NoDataFoundError, ValidationError, BadRequestError


class UpdateView:
    """
    A base view class for updating objects with query params.
    Attributes:
        manager (object): The manager instance responsible for handling database queries.
        serializer_class (object): The serializer class responsible for validating and serializing data.
    """

    manager: Manager = None
    lookup_field: str = None
    serializer_class: serializers.Serializer = None

    @classmethod
    def get_method_view_mapping(cls, patch=True):
        if patch:
            return {PATCH: "update", PUT: "update"}
        return {PUT: "update"}

    def add_common_update_data(self, data: dict | list, request):
        """
        Adds common metadata fields to the object, such as `created_by` and `updated_by`.

        Args:
            data (dict | list): The input data to be updated with common metadata.
            request (Request): The HTTP request containing user information.
            many (bool): Determines if multiple objects are being processed.

        Returns:
            dict | list: The updated data with additional metadata fields.
        """

        data["updated_by"] = request.user.user_id

        return data

    def update(self, request, **kwargs):
        """
        Update an object based on query params and data provided in the request.
        Args:
            request (Request): The HTTP request object containing the data.
        Returns:
            object: The updated object if the update is successful.
        """
        query = {
            self.lookup_field: kwargs[self.lookup_field],
        }

        obj = self.manager.get(query=query)
        if not obj:
            raise NoDataFoundError()

        is_partial = request.method == PATCH.upper()

        serializer = self.serializer_class(obj, data=request.data, partial=is_partial)

        is_valid = serializer.is_valid()
        if not is_valid:
            raise ValidationError(serializer.errors)

        data = serializer.validated_data

        if not data:
            raise BadRequestError(error.DATA_NOT_PROVIDED)

        data = self.add_common_update_data(data=data, request=request)

        obj = self.manager.update(data, query)

        return generate_response(
            data=obj.to_dict(),
            status_code=status.HTTP_200_OK,
            messages={"message": success.UPDATED_SUCCESSFULLY},
        )
