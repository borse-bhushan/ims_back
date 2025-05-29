"""
This file is to update the version of the application.
"""

import logging

from django.core.management.base import BaseCommand, CommandError

from utils.logger import logger
from utils import version as v_action, constants


DOC = """
This cmd is to update the version of the application.

If there is an new module added in the application then it will considered as Major Update. To make a Major
update type MJ parameter.

If there is an small functionality is added into the any feature then it will be considered as Miner Update.
For Minor update type MN parameter.

IF there is an bug fix then For Bug Fixes type BF parameter.

To print the current version you can pass the CV parameter.

python manage.py ver <version_update_type>
e.g python manage.py ver MJ.
"""


def get_choices():
    """
    These function will return the choices of option you can provide to cmd.
    And it will convert them into lower and upper case user can pass the cmd options in both case.
    """
    choices = [
        constants.MAJOR_VERSION,
        constants.MINOR_VERSION,
        constants.BUG_FIX,
        constants.CURRENT_VERSION,
    ]
    return choices + [choice.lower() for choice in choices]


class Command(BaseCommand):
    help = DOC
    __doc__ = DOC

    CMD = constants.CMD

    CHOICES = get_choices()

    def handle(self, *args, **kwargs):
        """
        Handle the user given cmd and return the result.
        """

        v_type: str = kwargs[constants.VERSION_TYPE].upper()

        if v_type == constants.CURRENT_VERSION:
            o_v = v_action.get_version_str()
            self.stdout.write(f"The current version is {o_v}")
            return ""

        version_data: dict = v_action.read_version()
        if v_type not in version_data:
            version_types = ", ".join(version_data)
            raise CommandError(
                f"({v_type}) is wrong, Available version type are {version_types}"
            )

        o_v = v_action.get_version_str()

        version_data[v_type] += 1

        if v_type == constants.MAJOR_VERSION:
            version_data[constants.MINOR_VERSION] = 0
            version_data[constants.BUG_FIX] = 0

        if v_type == constants.MINOR_VERSION:
            version_data[constants.BUG_FIX] = 0

        v_action.write_version(version_data)

        n_v = v_action.get_version_str()

        logger.log_msg(logging.INFO, f"Version is updated  [{o_v}  >>  {n_v}]")
        return ""

    def add_arguments(self, parser):
        """
        Add the needed arguments for these function to work.
        """
        parser.add_argument(
            constants.VERSION_TYPE,
            choices=self.CHOICES,
            type=str,
            help="""
                Which type of update you want Major(MJ), Miner(MN), Bug Fixes(BF), Current Version(CV).
            """,
        )
