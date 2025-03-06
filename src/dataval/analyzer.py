"""Data validators for common data types."""

import re
from datetime import datetime


def is_email(value: str) -> bool:
    """
    Validate if a string is a valid email address.

    Args:
        value: String to validate

    Returns:
        True if valid email, False otherwise
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, value))


def is_url(value: str) -> bool:
    """
    Validate if a string is a valid URL.

    Args:
        value: String to validate

    Returns:
        True if valid URL, False otherwise
    """
    pattern = r"^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$"
    return bool(re.match(pattern, value))


def is_credit_card(value: str) -> bool:
    """
    Validate if a string is a valid credit card number using Luhn algorithm.

    Args:
        value: String to validate

    Returns:
        True if valid credit card number, False otherwise
    """
    # Remove any spaces or hyphens
    value = value.replace(" ", "").replace("-", "")

    # Check if all characters are digits
    if not value.isdigit():
        return False

    # Check length (most credit cards are between 13-19 digits)
    if not 13 <= len(value) <= 19:
        return False

    # Luhn algorithm
    digits = [int(d) for d in value]
    checksum = 0
    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:  # odd positions (from right)
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit

    return checksum % 10 == 0


def is_date(value: str, format_str: str = "%Y-%m-%d") -> bool:
    """
    Validate if a string is a valid date in the given format.

    Args:
        value: String to validate
        format_str: Date format string (default: "%Y-%m-%d")

    Returns:
        True if valid date, False otherwise
    """
    try:
        datetime.strptime(value, format_str)
        return True
    except ValueError:
        return False


def is_number_in_range(
    value: int | float,
    min_val: int | float | None = None,
    max_val: int | float | None = None,
) -> bool:
    """
    Validate if a number is within a specified range.

    Args:
        value: Number to validate
        min_val: Minimum allowed value (inclusive)
        max_val: Maximum allowed value (inclusive)

    Returns:
        True if in range, False otherwise
    """
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True
