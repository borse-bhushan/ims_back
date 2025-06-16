"""
Load data from files into the database.
# This command reads data from predefined files and populates the database with the necessary
"""

from django.core.management.base import BaseCommand

from utils.logger import log_msg, logging
from utils.load_data.load import load_data


class Command(BaseCommand):
    """
    Command to load data from files into the database.
    """

    def handle(self, *args, **kwargs):
        """
        Handle the command to load data from files.
        This method is called when the command is executed.
        """
        log_msg(logging.INFO, "Loading data from files...")
        load_data()
        log_msg(logging.INFO, "Data loaded successfully.")

        return ""
