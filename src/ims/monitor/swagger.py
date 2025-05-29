"""
Serializers for the system information API.
"""

from rest_framework import serializers


class DiskInfoSerializer(serializers.Serializer):
    """
    Serializer for Disk-related system information.
    """

    total = serializers.CharField(help_text="Total disk space available.")
    used = serializers.CharField(help_text="Total disk space used.")
    free = serializers.CharField(help_text="Total disk space free.")
    percent = serializers.CharField(help_text="Percentage of disk space used.")
    read_count = serializers.IntegerField(help_text="Number of disk read operations.")
    write_count = serializers.IntegerField(help_text="Number of disk write operations.")


class MemoryInfoSerializer(serializers.Serializer):
    """
    Serializer for Memory-related system information.
    """

    percent = serializers.CharField(help_text="Percentage of memory used.")
    total = serializers.CharField(help_text="Total system memory (GB and MB).")
    used = serializers.CharField(help_text="Memory currently in use (GB and MB).")
    free = serializers.CharField(help_text="Memory currently free (GB and MB).")
    available = serializers.CharField(help_text="Memory available for use (GB and MB).")


class CPUInfoSerializer(serializers.Serializer):
    """
    Serializer for CPU-related system information.
    """

    percent_per_core = serializers.CharField(help_text="CPU usage percentage per core.")
    percent_total = serializers.CharField(help_text="Total CPU usage percentage.")
    count_logical = serializers.IntegerField(
        help_text="Total number of logical CPU cores."
    )
    count_physical = serializers.IntegerField(
        help_text="Total number of physical CPU cores."
    )
    frequency_current = serializers.CharField(help_text="Current CPU frequency in MHz.")
    frequency_min = serializers.CharField(help_text="Minimum CPU frequency in MHz.")
    frequency_max = serializers.CharField(help_text="Maximum CPU frequency in MHz.")
    times_user = serializers.CharField(
        help_text="Total time CPU spent in user mode (in seconds)."
    )
    times_system = serializers.CharField(
        help_text="Total time CPU spent in system mode (in seconds)."
    )
    times_idle = serializers.CharField(
        help_text="Total time CPU spent in idle state (in seconds)."
    )


class SysInfoDataSerializer(serializers.Serializer):
    """
    Serializer for overall system information, including CPU, Disk, and Memory details.
    """

    cpu = CPUInfoSerializer(help_text="CPU-related system information.")
    disk = DiskInfoSerializer(help_text="Disk-related system information.")
    memory = MemoryInfoSerializer(help_text="Memory-related system information.")


class SysInfoResponseSerializer(serializers.Serializer):
    """
    Serializer for the system information API response.
    """

    data = SysInfoDataSerializer(
        help_text="System information data containing CPU, Disk, and Memory details."
    )
    errors = serializers.JSONField(
        help_text="Any errors encountered during data retrieval.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages.", allow_null=True
    )
    status_code = serializers.IntegerField(
        help_text="HTTP status code of the response."
    )
    is_success = serializers.BooleanField(
        help_text="Indicates whether the request was successful."
    )
