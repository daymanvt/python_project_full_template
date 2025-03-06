#!/usr/bin/env python3
"""
Demo application entry point.

This script demonstrates both packages:
- mypackage1: CLI text utilities
- mypackage2: Data validation library
"""

import argparse

from rich.console import Console
from rich.panel import Panel

import mypackage1.module1 as text_analysis
import mypackage1.module2 as text_transform
import mypackage2.module1 as validators
import mypackage2.module2 as transformers
from mypackage2.subpackage.module3 import Field, Schema


def demo_text_utils(sample_text: str) -> None:
    """Demonstrate text utilities from mypackage1."""
    console = Console()

    console.print(
        Panel.fit("[bold green]Text Utilities Demo[/]", border_style="green")
    )

    console.print("[bold]Sample Text:[/]")
    console.print(sample_text)
    console.print("")

    # Demonstrate text analysis
    console.print("[bold cyan]Text Analysis:[/]")
    console.print(f"Word Count: {len(sample_text.split())}")
    console.print(
        f"Sentence Count: {text_analysis.sentence_count(sample_text)}"
    )
    console.print(
        f"Average Word Length: \
            {text_analysis.average_word_length(sample_text):.2f}"
    )

    # Demonstrate top words
    console.print("\n[bold cyan]Top 5 Words:[/]")
    for word, count in text_analysis.get_top_words(sample_text, n=5):
        console.print(f"{word}: {count}")

    # Demonstrate text transformation
    console.print("\n[bold cyan]Text Transformations:[/]")
    title = "Python Programming Language"
    console.print(f"Original: {title}")
    console.print(f"Slugified: {text_transform.slugify(title)}")
    console.print(
        f"Truncated: {text_transform.truncate(sample_text, length=50)}"
    )


def demo_data_validation() -> None:
    """Demonstrate data validation from mypackage2."""
    console = Console()

    console.print(
        Panel.fit("[bold blue]Data Validation Demo[/]", border_style="blue")
    )

    # Demonstrate basic validators
    console.print("[bold cyan]Basic Validators:[/]")

    test_email = "user@example.com"
    console.print(
        f"Is '{test_email}' a valid email? {validators.is_email(test_email)}"
    )

    test_url = "https://www.example.com"
    console.print(
        f"Is '{test_url}' a valid URL? {validators.is_url(test_url)}"
    )

    test_date = "2023-05-15"
    console.print(
        f"Is '{test_date}' a valid date? {validators.is_date(test_date)}"
    )

    # Demonstrate transformers
    console.print("\n[bold cyan]Data Transformers:[/]")

    test_string = "Hello World Example"
    console.print(f"Original: {test_string}")
    console.print(f"Snake Case: {transformers.to_snake_case(test_string)}")
    console.print(f"Camel Case: {transformers.to_camel_case(test_string)}")

    # Demonstrate schema validation
    console.print("\n[bold cyan]Schema Validation:[/]")

    # Define a user schema
    user_schema = Schema(
        {
            "username": Field(str, validators=[lambda s: len(s) >= 3]),
            "email": Field(str, validators=[validators.is_email]),
            "age": Field(int, validators=[lambda n: n >= 18]),
            "website": Field(
                str, required=False, validators=[validators.is_url]
            ),
        }
    )

    # Valid user data
    valid_user = {
        "username": "johndoe",
        "email": "john@example.com",
        "age": 25,
        "website": "https://example.com",
    }

    # Invalid user data
    invalid_user = {
        "username": "jd",  # too short
        "email": "not-an-email",
        "age": 16,  # under 18
    }

    console.print("Valid user schema check:", user_schema.is_valid(valid_user))

    console.print("Invalid user validation errors:")
    errors = user_schema.validate(invalid_user)
    for field, field_errors in errors.items():
        console.print(f"  {field}: {', '.join(field_errors)}")


def run_cmd_example() -> None:
    """Run the cmd example."""
    try:
        import cmd_example  # pylint: disable=C0415

        cmd_example.main()
    except ImportError:
        console = Console()
        console.print("[bold red]Error:[/] cmd_example.py not found")


def run_unittest_example() -> None:
    """Run the unittest example."""
    try:
        import unittest  # pylint: disable=C0415

        import tests.unittest_example  # pylint: disable=C0415

        unittest.main(module=tests.unittest_example)
    except ImportError:
        console = Console()
        console.print(
            "[bold red]Error:[/] \
                      tests/unittest_example.py not found"
        )


def main() -> None:
    """Main entry point for the demo application."""
    parser = argparse.ArgumentParser(description="Delta-313 Demo Application")
    parser.add_argument(
        "--demo",
        choices=["text", "data", "all", "cmd", "unittest"],
        default="all",
        help="Which demo to run",
    )

    args = parser.parse_args()

    with open("sample.txt", encoding="utf-8") as f:
        text = f.read()

    if args.demo == "cmd":
        run_cmd_example()
        return

    if args.demo == "unittest":
        run_unittest_example()
        return

    if args.demo in ["text", "all"]:
        demo_text_utils(text)
        print("\n" + "-" * 50 + "\n")

    if args.demo in ["data", "all"]:
        demo_data_validation()


if __name__ == "__main__":
    main()
