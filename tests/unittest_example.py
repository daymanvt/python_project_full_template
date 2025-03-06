#!/usr/bin/env python3
"""
Example of using the unittest package for testing delta-313.
This example provides an alternative to pytest for unit testing.
"""

import unittest

# Import functions from textkit
from textkit.analyzer import (
    average_word_length,
    sentence_count,
    word_frequency,
)
from textkit.transformer import replace_all, slugify, truncate

# Import functions from dataval
from dataval.validators import is_date, is_email, is_url
from dataval.transformers import to_camel_case, to_snake_case
from dataval.validation.schema import Field, Schema


class TestTextkit(unittest.TestCase):
    """Test cases for textkit using unittest."""

    def setUp(self):
        """Set up test fixtures."""
        self.sample_text = "Hello world. This is a test. Python is great!"
        self.replacements = {"Hello": "Hi", "great": "awesome"}

    def test_word_frequency(self):
        """Test word frequency calculation."""
        result = word_frequency(self.sample_text)
        self.assertEqual(result["hello"], 1)
        self.assertEqual(result["world"], 1)
        self.assertEqual(result["is"], 2)  # "is" appears twice

    def test_average_word_length(self):
        """Test average word length calculation."""
        result = average_word_length(self.sample_text)
        # Calculate expected result manually
        words = self.sample_text.lower().split()
        expected = sum(len(word) for word in words) / len(words)
        self.assertAlmostEqual(result, expected)

    def test_sentence_count(self):
        """Test sentence counting."""
        result = sentence_count(self.sample_text)
        self.assertEqual(result, 3)

    def test_slugify(self):
        """Test slugify function."""
        test_cases = [
            ("Hello World", "hello-world"),
            ("Python 3.9", "python-3-9"),
            ("Special@#$% Characters", "special-characters"),
        ]

        for input_text, expected in test_cases:
            with self.subTest(input=input_text):
                self.assertEqual(slugify(input_text), expected)

    def test_truncate(self):
        """Test text truncation."""
        temp = truncate("Hello World", length=6)
        print(f"\n\ntemp: {temp}\n\n")
        self.assertEqual(truncate("Hello World", length=8), "Hello...")
        self.assertEqual(truncate("Short", length=10), "Short")

    def test_replace_all(self):
        """Test multiple replacements."""
        result = replace_all(self.sample_text, self.replacements)
        self.assertEqual(result, "Hi world. This is a test. Python is awesome!")


class TestDataval(unittest.TestCase):
    """Test cases for dataval using unittest."""

    def test_validators(self):
        """Test validator functions."""
        # Test email validation
        valid_emails = ["user@example.com", "name.surname+tag@domain.co.uk"]
        invalid_emails = ["not-an-email", "@example.com", "user@", "user@.com"]

        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_email(email))

        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_email(email))

        # Test URL validation
        valid_urls = ["https://example.com", "http://test.com/path?query=1"]
        invalid_urls = ["not-a-url", "example.com", "https://"]

        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(is_url(url))

        for url in invalid_urls:
            with self.subTest(url=url):
                self.assertFalse(is_url(url))

        # Test date validation
        self.assertTrue(is_date("2023-05-15"))
        self.assertFalse(is_date("2023/05/15"))  # Wrong format

    def test_transformers(self):
        """Test transformer functions."""
        # Test snake case
        self.assertEqual(to_snake_case("HelloWorld"), "hello_world")
        self.assertEqual(to_snake_case("User Name"), "user_name")

        # Test camel case
        self.assertEqual(to_camel_case("hello world"), "helloWorld")
        self.assertEqual(
            to_camel_case("first_second_third"), "firstSecondThird"
        )

    def test_schema(self):
        """Test schema validation."""
        # Create a schema
        user_schema = Schema(
            {
                "name": Field(str, validators=[lambda s: len(s) >= 3]),
                "age": Field(int, validators=[lambda n: n >= 18]),
                "email": Field(str, required=False),
            }
        )

        # Test valid data
        valid_data = {"name": "John", "age": 25}
        self.assertTrue(user_schema.is_valid(valid_data))

        # Test invalid data
        invalid_data_1 = {"name": "Jo", "age": 25}  # Name too short
        self.assertFalse(user_schema.is_valid(invalid_data_1))

        invalid_data_2 = {"name": "John", "age": 16}  # Age too low
        self.assertFalse(user_schema.is_valid(invalid_data_2))

        # Test missing required field
        invalid_data_3 = {"age": 25}  # Missing name
        self.assertFalse(user_schema.is_valid(invalid_data_3))


if __name__ == "__main__":
    unittest.main()
