"""
This module provides a Pagination class to handle pagination of data.
It takes the total count of items, the current page number, and the page size.
It provides methods to get the current page objects and the total number of pages.
The Pagination class is initialized with the total count of items,
the current page number, and the page size.
The class also provides a default page size of 10 items per page.
"""


class Pagination:
    __doc__ = """
    This class is used to handle pagination of data.
    It takes the total count of items, the current page number, and the page size.
    It provides methods to get the current page objects and the total number of pages.
    """

    def __init__(self, count: int, current_page: int, page_size: int):
        self.count = count
        self.page_size = page_size
        self.current_page = current_page

    def get_current_page_objs(self, data: list):
        """
        This method returns the current page objects based on the current page and page size.
        :param data: The data to be paginated.
        :return: The current page objects.
        """
        if not self.count:
            return []

        start_index: int = (self.current_page - 1) * self.page_size
        end_index = start_index + self.page_size
        return data[start_index:end_index]

    def get_total_page_count(self):
        """
        This method returns the total number of pages based on the count and page size.
        :return: The total number of pages.
        """
        if not self.count:
            return 0
        return (self.count + self.page_size - 1) // self.page_size
