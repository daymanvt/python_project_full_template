"""Advanced text processing utilities."""

import re


def extract_hashtags(text: str) -> list[str]:
    """
    Extract hashtags from text.

    Args:
        text: The input text

    Returns:
        List of hashtags without the # symbol
    """
    pattern = r"#(\w+)"
    return re.findall(pattern, text)


def calculate_readability(text: str) -> dict[str, float] | dict[str, str]:
    """
    Calculate basic readability metrics.

    Args:
        text: The input text

    Returns:
        Dictionary with various readability scores
    """
    word_count = len(text.split())
    sentence_count = len(re.split(r"[.!?]+", text)) - 1
    char_count = len(text)

    if word_count == 0 or sentence_count == 0:
        return {"error": "Text too short for analysis"}

    avg_words_per_sentence = word_count / max(1, sentence_count)
    avg_chars_per_word = char_count / max(1, word_count)

    # Simple Flesch-Kincaid grade level approximation
    fk_grade = 0.39 * avg_words_per_sentence + 11.8 * avg_chars_per_word - 15.59

    return {
        "words_per_sentence": round(avg_words_per_sentence, 2),
        "chars_per_word": round(avg_chars_per_word, 2),
        "fk_grade_level": round(fk_grade, 2),
    }


def summarize(text: str, sentence_count: int = 3) -> str:
    """
    Create a simple extractive summary by selecting top sentences.

    Args:
        text: The input text
        sentence_count: Number of sentences to include in summary

    Returns:
        Summarized text
    """
    sentences = re.split(r"(?<=[.!?])\s+", text)
    if len(sentences) <= sentence_count:
        return text

    # Very simple algorithm - just take first few sentences
    # In a real implementation, you'd use more sophisticated methods
    return " ".join(sentences[:sentence_count])
