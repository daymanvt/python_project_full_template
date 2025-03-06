"""Text analysis utilities."""

import re
from collections import Counter


def word_frequency(text: str) -> dict[str, int]:
    """
    Calculate word frequency in a given text, ignoring punctuation.

    Args:
        text: The input text to analyze

    Returns:
        Dictionary with words as keys and their frequency as values
    """
    # Remove punctuation and convert to lowercase
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text).lower()
    words = text.split()
    return dict(Counter(words))


def get_top_words(text: str, n: int = 10) -> list[tuple[str, int]]:
    """
    Get the top N most frequent words.

    Args:
        text: The input text to analyze
        n: Number of top words to return (default: 10)

    Returns:
        List of (word, frequency) tuples for the top N words
    """
    frequencies = word_frequency(text)
    return sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[:n]


def average_word_length(text: str) -> float:
    """
    Calculate the average word length in a text.

    Args:
        text: The input text to analyze

    Returns:
        Average word length as a float
    """
    words = text.lower().split()
    if not words:
        return 0.0
    return sum(len(word) for word in words) / len(words)


def sentence_count(text: str) -> int:
    """
    Count the number of sentences in a text.

    Args:
        text: The input text to analyze

    Returns:
        Number of sentences
    """
    # Simple heuristic: Count periods, exclamation marks, and question marks
    return sum(1 for char in text if char in (".", "!", "?"))
