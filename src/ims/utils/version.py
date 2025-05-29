"""
This file will handle the version of the project.
"""

import json
from utils import constants

PATH = "config/ver.json"


class VersionData:
    """
    This class will hold the version data.
    """

    def __init__(self, version_info: dict = None):
        self.version_info = version_info or {}

    def set_version(self, version_info: dict):
        """
        Set the version info.
        """
        self.version_info = version_info
        return True


version_obj = VersionData()


def read_version():
    """
    Read the version json from the version file.
    """
    if version_obj.version_info:
        return version_obj.version_info

    with open(PATH, "r", encoding="UTF-8") as file:
        version_str: str = file.read()
        version_obj.set_version(json.loads(version_str))

    return version_obj.version_info


def get_version_str():
    """
    It will return the version str. [V1.1.1]
    """
    v_dict: dict = read_version()

    v_s = (
        f"V{v_dict[constants.MAJOR_VERSION]}.{v_dict[constants.MINOR_VERSION]}"
        f".{v_dict[constants.BUG_FIX]}"
    )

    return v_s


def write_version(version: dict):
    """
    write the new version into the file.
    """

    with open(PATH, "w", encoding="UTF-8") as file:
        json.dump(version, file)

    return True
