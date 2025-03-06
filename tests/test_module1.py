"""Tests for text utilities and data validators."""

from mypackage1.module1 import (
    average_word_length,
    get_top_words,
    sentence_count,
    word_frequency,
)
from mypackage2.module1 import (
    is_date,
    is_email,
    is_number_in_range,
    is_url,
)


# mypackage1.module1 tests
class TestTextAnalysis:
    """Test suite for text analysis functions."""

    def test_word_frequency(self):
        """Test word frequency calculation."""
        text = "hello world hello"
        result = word_frequency(text)
        assert result == {"hello": 2, "world": 1}

    def test_get_top_words(self):
        """Test getting top words by frequency."""
        text = "a b c a b a"
        result = get_top_words(text, n=2)
        assert result == [("a", 3), ("b", 2)]

    def test_average_word_length(self):
        """Test average word length calculation."""
        text = "hello a world"
        result = average_word_length(text)
        assert result == (5 + 1 + 5) / 3

    def test_sentence_count(self):
        """Test sentence counting."""
        text = "Hello. This is a test! How are you?"
        assert sentence_count(text) == 3

        empty_text = ""
        assert sentence_count(empty_text) == 0


# mypackage2.module1 tests
class TestValidators:
    """Test suite for data validators."""

    def test_is_email(self):
        """Test email validation."""
        assert is_email("user@example.com")
        assert is_email("user.name+tag@example.co.uk")
        assert not is_email("not-an-email")
        assert not is_email("@example.com")

    def test_is_url(self):
        """Test URL validation."""
        assert is_url("https://example.com")
        assert is_url("http://subdomain.example.com/path?query=1")
        assert not is_url("not a url")
        assert not is_url("example.com")  # Missing protocol

    def test_is_date(self):
        """Test date validation."""
        assert is_date("2023-05-15")
        assert is_date("05/15/2023", format_str="%m/%d/%Y")
        assert not is_date("not-a-date")
        assert not is_date("2023/05/15")  # Wrong format

    def test_is_number_in_range(self):
        """Test number range validation."""
        assert is_number_in_range(5, min_val=1, max_val=10)
        assert is_number_in_range(1, min_val=1, max_val=10)  # Edge case
        assert is_number_in_range(10, min_val=1, max_val=10)  # Edge case
        assert not is_number_in_range(0, min_val=1, max_val=10)
        assert not is_number_in_range(11, min_val=1, max_val=10)
