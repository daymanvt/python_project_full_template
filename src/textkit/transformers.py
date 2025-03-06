"""Text transformation utilities."""

import re


def slugify(text: str) -> str:
    """
    Convert text to slug format (lowercase, hyphens instead of spaces).

    Args:
        text: The input text to slugify

    Returns:
        Slugified text
    """
    text = text.lower()
    # Replace all non-alphanumeric characters with spaces
    text = re.sub(r"[^a-z0-9]", " ", text)
    # Replace consecutive spaces with a single hyphen
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


def truncate(text: str, length: int = 100, suffix: str = "...") -> str:
    """
    Truncate text to a specified length, adding a suffix if truncated.

    Args:
        text: The input text to truncate
        length: Maximum length (default: 100, minimum: 5)
        suffix: String to append if text is truncated (default: "...")

    Returns:
        Truncated text

    Raises:
        ValueError: If length is less than 5.
    """
    if length < 5:
        raise ValueError("Length must be at least 5")

    if len(text) <= length:
        return text
    return text[: length - len(suffix)] + suffix


def replace_all(text: str, replacements: dict[str, str]) -> str:
    """
    Replace multiple substrings in text based on a dictionary.

    Args:
        text: The input text
        replacements: Dictionary mapping substrings to their replacements

    Returns:
        Text with all replacements applied
    """
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def extract_emails(text: str) -> list[str]:
    """
    Extract email addresses from text.

    Args:
        text: The input text to search

    Returns:
        List of email addresses found
    """
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)
