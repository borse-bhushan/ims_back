"""
This file contains the constants used for the utility.
"""

from django.db import models


QA = "QA"
UAT = "UAT"
DEV = "DEV"
PROD = "PROD"
LOCAL = "LOCAL"


CMD = "ver"
VERSION_TYPE = "part"

MAJOR_VERSION = "MJ"
MINOR_VERSION = "MN"
BUG_FIX = "BF"
CURRENT_VERSION = "CV"

DATE_FORMAT = "%d-%m-%Y"

BASE_PATH: str = "/api"


class CurrencyCodeEnum(models.TextChoices):
    """
    Enum for ISO 4217 currency codes with symbols.
    """

    USD = "USD", "$"  # US Dollar
    EUR = "EUR", "€"  # Euro
    GBP = "GBP", "£"  # British Pound
    JPY = "JPY", "¥"  # Japanese Yen
    AUD = "AUD", "A$"  # Australian Dollar
    CAD = "CAD", "C$"  # Canadian Dollar
    CHF = "CHF", "CHF"  # Swiss Franc
    CNY = "CNY", "¥"  # Chinese Yuan
    INR = "INR", "₹"  # Indian Rupee
    BRL = "BRL", "R$"  # Brazilian Real
    RUB = "RUB", "₽"  # Russian Ruble
    ZAR = "ZAR", "R"  # South African Rand
    SEK = "SEK", "kr"  # Swedish Krona
    NOK = "NOK", "kr"  # Norwegian Krone
    NZD = "NZD", "NZ$"  # New Zealand Dollar
    SGD = "SGD", "S$"  # Singapore Dollar
    MXN = "MXN", "Mex$"  # Mexican Peso
    HKD = "HKD", "HK$"  # Hong Kong Dollar
    KRW = "KRW", "₩"  # South Korean Won
    TRY = "TRY", "₺"  # Turkish Lira
