"""
Address serializers module.
"""

from .address import CreateAddressSerializer
from .swagger import (
    AddressListResponseSerializer,
    AddressResponseSerializer,
    address_create_success_example,
    address_list_success_example,
    address_getById_success_example,
    address_update_success_example,
    address_delete_success_example
)
__all__ = [
    "CreateAddressSerializer",
    "AddressListResponseSerializer",
    "AddressResponseSerializer",
    "address_create_success_example",   
    "address_list_success_example", 
    "address_getById_success_example",
    "address_update_success_example",
    "address_delete_success_example"
]
