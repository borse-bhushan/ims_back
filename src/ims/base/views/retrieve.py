"""
This module contains the BaseGetView class, which provides a base implementation
for retrieving an object based on its ID. It raises a 404 error if the object is not found.
"""

from base import constants
from base.db_access import Manager
from utils.exceptions import NoDataFoundError
from utils.response import generate_response


class RetrieveView:
    """
    A base view class for retrieving object by their ID.
    Attributes:
        manager (object): The manager instance responsible for handling database queries.
    """

    manager: Manager = None
    lookup_field: str = None

    @classmethod
    def get_method_view_mapping(cls):
        """
        Returns a mapping of HTTP methods to view methods for this class.
        """
        return {constants.GET: "retrieve"}

    def get_details(self, obj, **kwargs):
        """
        Get the details of the object in dictionary format.
        """
        return obj.to_dict()

    def get_details_query(self, **kwargs):
        """
        Get the query parameters for retrieving the object based on the lookup field.
        """
        return {self.lookup_field: kwargs[self.lookup_field]}

    def retrieve(self, request, **kwargs):
        """
        Retrieve an object based on the ID provided in the request data.
        Args:
            request (Request): The HTTP request object containing the data.
        Returns:
            object: The retrieved object if found.
        """

        obj = self.manager.get(query=self.get_details_query(**kwargs, request=request))

        if not obj:
            raise NoDataFoundError()

        return generate_response(data=self.get_details(obj, request=request, **kwargs))
