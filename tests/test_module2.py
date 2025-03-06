"""Tests for transformers and text transformations."""

import pytest

from textkit.transformer import (
    extract_emails,
    replace_all,
    slugify,
    truncate,
)
from dataval.transformers import (
    format_date,
    to_camel_case,
    to_snake_case,
    to_title_case,
)
from dataval.validation.schema import Field, Schema


# textkit.transformer tests
class TestTextTransformations:
    """Test suite for text transformation functions."""

    def test_slugify(self):
        """Test slugify function."""
        assert slugify("Hello World") == "hello-world"
        assert slugify("Testing 123") == "testing-123"
        assert slugify("Special@#$% Characters") == "special-characters"

    def test_truncate(self):
        """Test text truncation."""
        assert truncate("Hello World", length=5) == "He..."
        assert truncate("Short", length=10) == "Short"

    def test_replace_all(self):
        """Test multiple replacements."""
        replacements = {"cat": "dog", "quick": "slow"}
        text = "The quick cat jumped"
        assert replace_all(text, replacements) == "The slow dog jumped"

    def test_extract_emails(self):
        """Test email extraction."""
        text = "Contact john@example.com or mary@test.org for more info."
        emails = extract_emails(text)
        assert "john@example.com" in emails
        assert "mary@test.org" in emails
        assert len(emails) == 2


# dataval.transformers tests
class TestDataTransformers:
    """Test suite for data transformation functions."""

    def test_to_snake_case(self):
        """Test conversion to snake_case."""
        assert to_snake_case("HelloWorld") == "hello_world"
        assert to_snake_case("API Response") == "api_response"
        assert to_snake_case("user-name") == "user_name"

    def test_to_camel_case(self):
        """Test conversion to camelCase."""
        assert to_camel_case("hello world") == "helloWorld"
        assert to_camel_case("snake_case_example") == "snakeCaseExample"
        assert to_camel_case("") == ""

    def test_to_title_case(self):
        """Test conversion to Title Case."""
        assert to_title_case("hello world") == "Hello World"
        assert to_title_case("SHOUTING TEXT") == "Shouting Text"

    def test_format_date(self):
        """Test date formatting."""
        assert (
            format_date("2023-05-15", output_format="%d/%m/%Y") == "15/05/2023"
        )
        with pytest.raises(ValueError):
            format_date("invalid-date")


# dataval.validation.schema tests
class TestSchema:
    """Test suite for schema validation."""

    def test_field_validation(self):
        """Test field validation."""
        field = Field(int, validators=[lambda x: x > 0])
        assert not field.validate(5)  # No errors
        assert field.validate(-5)  # Should have errors
        assert field.validate("not an int")  # Should have errors

    def test_schema_validation(self):
        """Test schema validation."""
        schema = Schema(
            {
                "name": Field(str, validators=[lambda s: len(s) > 0]),
                "age": Field(int, validators=[lambda n: n >= 18]),
                "email": Field(str, required=False),
            }
        )

        valid_data = {"name": "John", "age": 25}
        invalid_data = {"name": "", "age": 15}

        assert schema.is_valid(valid_data)
        assert not schema.is_valid(invalid_data)
