"""Helper functions for file management.
This module contains functions to handle file uploads and metadata storage.
"""

import os

from utils import settings
from utils.functions import get_uuid

from file.db_access import file_manager


def save_file(file, base_path):
    """
    Save the uploaded file to disk and store metadata in the database.

    Args:
        file (UploadedFile): The uploaded file from request.FILES.
        base_path (str): Subdirectory under MEDIA_ROOT to save the file.

    Returns:
        File: The created File DB record.
    """
    ext = file.name.split(".")[-1]
    file_id = get_uuid()
    file_name = f"{file_id}.{ext}"
    relative_path = os.path.join(base_path, file_name)
    absolute_path = os.path.join(settings.read("MEDIA_ROOT"), relative_path)

    os.makedirs(os.path.dirname(absolute_path), exist_ok=True)

    with open(absolute_path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    file_obj = file_manager.create(
        data={
            "file_id": file_id,
            "file_name": file.name,
            "file_size": file.size,
            "file_path": relative_path,
            "mime_type": file.content_type,
        }
    )

    return file_obj
