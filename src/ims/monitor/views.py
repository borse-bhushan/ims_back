"""
This file contains the monitoring API which will return the CPU, RAM, DISK information.
"""

import psutil
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from monitor import swagger

from auth_user.constants import MethodEnum
from utils.response import generate_response
from authentication import get_authentication_classes, register_permission


MODULE = "Monitor"


def get_memory_info():
    """
    This fun will return the memory information.
    """
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    memory_total_mb = memory_info.total / (1024 * 1024)
    memory_used_mb = memory_info.used / (1024 * 1024)
    memory_free_mb = memory_info.free / (1024 * 1024)
    memory_available_mb = memory_info.available / (1024 * 1024)

    memory_total_gb = memory_info.total / (1024 * 1024 * 1024)
    memory_used_gb = memory_info.used / (1024 * 1024 * 1024)
    memory_free_gb = memory_info.free / (1024 * 1024 * 1024)
    memory_available_gb = memory_info.available / (1024 * 1024 * 1024)

    return {
        "percent": f"{memory_percent}%",
        "total": f"[{memory_total_gb:.2f} GB] [{memory_total_mb} MB]",
        "used": f"[{memory_used_gb:.2f} GB] [{memory_used_mb} MB]",
        "free": f"[{memory_free_gb:.2f} GB] [{memory_free_mb} MB]",
        "available": f"[{memory_available_gb:.2f} GB] [{memory_available_mb} MB]",
    }


def get_cpu_info():
    """
    This fun will return the CPU information.
    """
    cpu_percent_per_core = psutil.cpu_percent(interval=1, percpu=True)
    cpu_percent_total = psutil.cpu_percent(interval=1)
    cpu_count_logical = psutil.cpu_count(logical=True)
    cpu_count_physical = psutil.cpu_count(logical=False)
    cpu_freq = psutil.cpu_freq()
    cpu_times = psutil.cpu_times()

    return {
        "percent_per_core": ", ".join(
            [
                f"Core{index + 1} {core}%"
                for index, core in enumerate(cpu_percent_per_core)
            ]
        ),
        "percent_total": f"{cpu_percent_total}%",
        "count_logical": cpu_count_logical,
        "count_physical": cpu_count_physical,
        "frequency_current": f"{cpu_freq.current} MHz",
        "frequency_min": f"{cpu_freq.min} MHz",
        "frequency_max": f"{cpu_freq.max} MHz",
        "times_user": f"{cpu_times.user} seconds",
        "times_system": f"{cpu_times.system} seconds",
        "times_idle": f"{cpu_times.idle} seconds",
    }


def get_disk_info():
    """
    This fun will return the disk information.
    """
    disk_usage = psutil.disk_usage("/")
    disk_io = psutil.disk_io_counters()

    return {
        "total": f"{disk_usage.total / (1024 * 1024 * 1024):.2f} GB",
        "used": f"{disk_usage.used / (1024 * 1024 * 1024):.2f} GB",
        "free": f"{disk_usage.free / (1024 * 1024 * 1024):.2f} GB",
        "percent": f"{disk_usage.percent}%",
        "read_count": disk_io.read_count,
        "write_count": disk_io.write_count,
    }


class MonitorView(APIView):
    __doc__ = """
        This is the monitoring API which will return the CPU, RAM, DISK information.
        get: this fun will return the system health details.
    """

    get_authenticators = get_authentication_classes

    @extend_schema(
        responses={"200": swagger.SysInfoResponseSerializer()},
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE} information", create_permission=False)
    def get(self, *_):
        """
        This API will return the system health details.
        """

        data = {
            "cpu": get_cpu_info(),
            "disk": get_disk_info(),
            "memory": get_memory_info(),
        }

        return generate_response(data=data)
