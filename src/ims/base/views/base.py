"""
Base view class for CRUD operations.
This class combines the functionality of CreateView, ListView,
RetrieveView, UpdateView, and DeleteView to provide a standard implementation
"""

from base.views import CreateView, ListView, RetrieveView, UpdateView, DeleteView


class BaseView(CreateView, ListView, RetrieveView, UpdateView, DeleteView):
    """
    A base view class that combines the functionality of CreateView, ListView,
    RetrieveView, UpdateView, and DeleteView. This class provides a standard
    implementation for handling CRUD operations on objects using the Manager class.
    """

    @classmethod
    def get_method_view_mapping(cls, with_path_id=False):
        if with_path_id:
            return {
                **UpdateView.get_method_view_mapping(),
                **DeleteView.get_method_view_mapping(),
                **RetrieveView.get_method_view_mapping(),
            }

        return {
            **ListView.get_method_view_mapping(),
            **CreateView.get_method_view_mapping(),
        }
