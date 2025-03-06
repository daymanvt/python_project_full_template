"""Data schema validation utilities."""

from collections.abc import Callable
from typing import Any


class Field:
    """Field definition for schema validation."""

    def __init__(
        self,
        field_type: type,
        required: bool = True,
        validators: list[Callable[[Any], bool]] | None = None,
        default: Any = None,
    ):
        """
        Initialize a field validator.

        Args:
            field_type: Expected Python type for the field
            required: Whether the field is required (default: True)
            validators: List of validator functions (default: None)
            default: Default value if field is missing (default: None)
        """
        self.field_type = field_type
        self.required = required
        self.validators = validators or []
        self.default = default

    def validate(self, value: Any) -> list[str]:
        """
        Validate a value against this field's rules.

        Args:
            value: Value to validate

        Returns:
            List of error messages (empty if valid)
        """
        errors = []

        # Check if field is present
        if value is None:
            if self.required:
                errors.append("Field is required")
            return errors

        # Type check
        if not isinstance(value, self.field_type):
            errors.append(
                f"Expected type {self.field_type.__name__}\
                    , got {type(value).__name__}"
            )
            # Return early - don't run validators on wrong type
            return errors

        # Run custom validators only if type check passes
        for validator in self.validators:
            try:
                if not validator(value):
                    errors.append(
                        f"Failed validation with {validator.__name__}"
                    )
            except ValueError as e:
                errors.append(f"Validation error: {str(e)}")

        return errors


class Schema:
    """Schema validator for structured data."""

    def __init__(self, fields: dict[str, Field]):
        """
        Initialize schema with field definitions.

        Args:
            fields: Dictionary mapping field names to Field objects
        """
        self.fields = fields

    def validate(self, data: dict[str, Any]) -> dict[str, list[str]]:
        """
        Validate data against schema.

        Args:
            data: Dictionary to validate

        Returns:
            Dictionary of field names to error messages
        """
        errors = {}

        # Check all fields defined in schema
        for field_name, field_def in self.fields.items():
            field_errors = field_def.validate(data.get(field_name))
            if field_errors:
                errors[field_name] = field_errors

        return errors

    def is_valid(self, data: dict[str, Any]) -> bool:
        """
        Check if data is valid according to schema.

        Args:
            data: Dictionary to validate

        Returns:
            True if valid, False otherwise
        """
        return len(self.validate(data)) == 0

    def apply_defaults(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Apply default values for missing fields.

        Args:
            data: Original data dictionary

        Returns:
            Data with default values applied
        """
        result = data.copy()

        for field_name, field_def in self.fields.items():
            if field_name not in result and field_def.default is not None:
                result[field_name] = field_def.default

        return result
