"""
File manager module.
This module contains the FileManager class, which is responsible for managing
the File model.
It provides methods for creating, updating, deleting, and retrieving file records.
"""

from base.db_access import manager

from .models import File


class FileManager(manager.Manager[File]):
    """
    Manager class for the File model.
    """

    model = File


file_manager = FileManager()
