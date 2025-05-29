from rest_framework import status

from base import constants
from base.db_access import Manager
from utils.messages import success
from utils.response import generate_response
from utils.exceptions import NoDataFoundError


class DeleteView:
    """
    A base view class for handling delete operations using the Manager class.

    This class provides a standard implementation for deleting objects,
    supporting both soft deletion (marking objects as deleted) and
    hard deletion (permanently removing them from the database).

    Attributes:
        manager (Manager): An instance responsible for database operations.
        lookup_field (str): The field used to identify the object for deletion.
    """

    manager: Manager = None
    lookup_field: str = None

    @classmethod
    def get_method_view_mapping(cls):
        return {constants.DELETE: "destroy"}

    def pre_delete(self, *_, **__):
        pass

    def post_delete(self, *_, **__):
        pass

    def destroy(self, request, **kwargs):
        """
        Handles the object deletion process.

        This method retrieves the object based on the lookup field
        and performs soft deletion by default. It allows customization
        of deletion behavior through the Manager class.

        Args:
            request (Request): The HTTP request containing relevant parameters.
            **kwargs: Additional keyword arguments, including the lookup field value.

        Returns:
            Response: A success response if deletion is successful.

        Raises:
            NoDataFoundError: If the required lookup parameter is missing.
        """
        query = {
            self.lookup_field: kwargs[self.lookup_field],
        }

        obj = self.manager.get(query=query)
        if not obj:
            raise NoDataFoundError()

        self.pre_delete(request=request, **kwargs)

        self.manager.delete(query=query)

        self.post_delete(request=request, **kwargs)

        return generate_response(
            data=None,
            messages={"message": success.DELETED_SUCCESSFULLY},
            status_code=status.HTTP_204_NO_CONTENT,
        )
