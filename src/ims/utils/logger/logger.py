"""
This module is used to log the messages.
"""

import logging
import inspect


from utils import functions, settings


def log_msg(level, *msg, sep="\n", ref_data: dict = None):
    """
    It's used to log the message.
    """

    caller_frame = inspect.currentframe().f_back
    caller_function_name = caller_frame.f_code.co_name

    msg_details = f"[FUNC:- {caller_function_name}] "

    if ref_data:
        ref_data_for_error = []
        for key, value in ref_data.items():
            ref_data_for_error.append(f"{key}:{value}")
        ref_data_for_error = " ".join(ref_data_for_error)
        msg_details += f"[REF_DATA:- {ref_data_for_error}]"

    msg_ = []

    if msg_details:
        msg_.append(msg_details)

    msg = sep.join(
        [
            *msg_,
            *msg,
            "---------------------------------------" * 3,
        ]
    )
    if functions.is_local() and functions.is_linux():
        if level == logging.ERROR:
            msg = f"[🐞] {msg}"
        if level == logging.DEBUG:
            msg = f"[🛠️] {msg}"
        if level == logging.INFO:
            msg = f"[📝] {msg}"
        if level == logging.WARNING:
            msg = f"[⚠️] {msg}"

    logger = logging.getLogger(settings.read("PROJECT_NAME"))
    if logger.level:
        logger.log(level, msg)
    else:
        logging.log(level=level, msg=msg)
