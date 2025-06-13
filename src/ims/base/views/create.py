"""
This module provides a base view class for handling create operations in a IMS application.
"""

from django.db import models
from rest_framework import status, serializers, parsers

from base import constants
from base.db_access import Manager


from utils.messages import success
from utils.response import generate_response
from utils.exceptions import ValidationError
from utils import functions as common_functions


class CreateView:
    """
    A base view class for handling create operations using the Manager class.
    This class provides a standard implementation for object creation,
    including validation, data processing, and database persistence.

    Attributes:
        many (bool): Indicates whether the operation handles multiple objects at once.
        manager (Manager): An instance responsible for handling database interactions.
        serializer_class (serializers.Serializer): The serializer used to validate input data.
    """

    many = False
    manager: Manager = None
    serializer_class = None
    is_common_data_needed = True

    parser_classes = (parsers.JSONParser, parsers.MultiPartParser)

    @classmethod
    def get_method_view_mapping(cls):
        """
        Returns a dictionary mapping HTTP methods to their corresponding view actions.
        """
        return {constants.POST: "create"}

    def post_save(self, obj: models.Model = None, **kwargs):
        """
        A hook executed after the object is saved in the database.
        This method allows additional modifications or operations on the saved object.

        Args:
            obj (models.Model): The saved object instance.
            **kwargs: Additional keyword arguments.

        Returns:
            models.Model: The modified object after post-save operations.
        """
        if self.many or obj is None:
            return generate_response(
                data=None,
                status_code=status.HTTP_201_CREATED,
                messages={"message": success.CREATED_SUCCESSFULLY},
            )

        return generate_response(
            data=obj.to_dict(),
            status_code=status.HTTP_201_CREATED,
            messages={"message": success.CREATED_SUCCESSFULLY},
        )

    def pre_save(self, data: dict | list, **kwargs):
        """
        A hook executed before saving the object.
        This method allows preprocessing of data, such as adding default values.

        Args:
            data (dict | list): The validated input data.
            **kwargs: Additional keyword arguments.

        Returns:
            dict | list: The processed data before saving.
        """

        return data

    def add_common_data(
        self,
        data: dict | list,
        request,
        many=False,
    ):
        """
        Adds common metadata fields to the object, such as `created_by` and `updated_by`.

        Args:
            data (dict | list): The input data to be updated with common metadata.
            request (Request): The HTTP request containing user information.
            many (bool): Determines if multiple objects are being processed.

        Returns:
            dict | list: The updated data with additional metadata fields.
        """
        user = request.user

        user_id = user.user_id

        def add_data(item: dict):
            """
            Adds common metadata to a single item.
            """
            item["created_by"] = user_id
            item["updated_by"] = user_id

            return item

        if many:
            data_list = []
            for item in data:
                data_list.append(add_data(item))

            return data_list

        return add_data(data)

    def save(self, data: dict | list, using=None, **kwargs):
        """
        Saves the validated data to the database using the manager.
        """
        return self.manager.create(data, many=self.many, using=using)

    def is_create_data_valid(self, request, *args, **kwargs):
        """
        Validates the input data for the create operation.
        """

        serializer_obj: serializers.Serializer = self.serializer_class(
            data=request.data, many=self.many
        )

        if not serializer_obj.is_valid():
            raise ValidationError(serializer_obj.errors)

        return serializer_obj.validated_data

    def create(self, request, *args, **kwargs):
        """
        Handles the object creation process, including validation, data enrichment,
        database persistence, and response generation.

        Args:
            request (Request): The HTTP request containing input data.

        Returns:
            Response: A success response with the created object(s)
            or an error message if validation fails.
        """

        data = self.is_create_data_valid(request, *args, **kwargs)

        if self.is_common_data_needed:
            data = self.add_common_data(data=data, request=request, many=self.many)

        data = self.pre_save(data=data, request=request)

        obj = self.save(data=data, request=request)

        return self.post_save(obj=obj, data=data, request=request)
