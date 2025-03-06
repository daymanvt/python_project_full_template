"""Data transformation utilities."""

import json
import re
from datetime import datetime
from typing import Any


def to_snake_case(text: str) -> str:
    """
    Convert string to snake_case.

    Args:
        text: String to convert

    Returns:
        snake_case string
    """
    # Replace non-alphanumeric characters with underscores
    result = re.sub(r"[^a-zA-Z0-9]+", "_", text)

    # Add underscore at the transition from lowercase to uppercase
    result = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", result)

    # Convert to lowercase and clean up
    result = result.lower().strip("_")

    # Remove duplicate underscores
    result = re.sub(r"_+", "_", result)

    return result


def to_camel_case(text: str) -> str:
    """
    Convert string to camelCase.

    Args:
        text: String to convert

    Returns:
        camelCase string
    """
    # Replace any non-alphanumeric character with space
    s1 = re.sub(r"[^a-zA-Z0-9]", " ", text)
    # Split, capitalize each word except first, and join
    words = s1.split()
    if not words:
        return ""

    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


def to_title_case(text: str) -> str:
    """
    Convert string to Title Case.

    Args:
        text: String to convert

    Returns:
        Title Case string
    """
    return " ".join(word.capitalize() for word in text.split())


def format_date(
    date_str: str,
    input_format: str = "%Y-%m-%d",
    output_format: str = "%B %d, %Y",
) -> str:
    """
    Format a date string from one format to another.

    Args:
        date_str: Date string to format
        input_format: Input date format (default: "%Y-%m-%d")
        output_format: Output date format (default: "%B %d, %Y")

    Returns:
        Formatted date string
    """
    date_obj = datetime.strptime(date_str, input_format)
    return date_obj.strftime(output_format)


def dict_to_json(data: dict[str, Any], pretty: bool = False) -> str:
    """
    Convert dictionary to JSON string.

    Args:
        data: Dictionary to convert
        pretty: Whether to format the JSON with indentation (default: False)

    Returns:
        JSON string
    """
    indent = 4 if pretty else None
    return json.dumps(data, indent=indent)
