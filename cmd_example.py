#!/usr/bin/env python3
"""
Interactive command shell example using the cmd package.
This example demonstrates an interactive shell for the delta-313 package.
"""

import cmd
import shlex

from mypackage1.module1 import (
    average_word_length,
    get_top_words,
)
from mypackage1.module2 import extract_emails, slugify, truncate
from mypackage2.module1 import is_date, is_email, is_url
from mypackage2.module2 import to_camel_case, to_snake_case, to_title_case


class Delta313Shell(cmd.Cmd):
    """Interactive command processor for delta-313 package."""

    intro = """
    Welcome to the Delta-313 Interactive Shell!
    Type 'help' or '?' to list commands.
    Type 'quit' or 'exit' to exit.
    """
    prompt = "delta313> "

    def do_analyze(self, arg: str) -> None:
        """
        Analyze text and show statistics.
        Usage: analyze "Your text here"
        """
        if not arg:
            print("Please provide text to analyze.")
            return

        try:
            text = shlex.split(arg)[0]
            print(f"\nText Analysis for: {text}\n" + "-" * 40)
            print(f"Word Count: {len(text.split())}")
            print(f"Character Count: {len(text)}")
            print(f"Average Word Length: {average_word_length(text):.2f}")

            # Show word frequency
            print("\nTop Words:")
            for word, count in get_top_words(text, n=5):
                print(f"  {word}: {count}")
        except Exception as e:
            print(f"Error: {e}")

    def do_transform(self, arg: str) -> None:
        """
        Transform text with different methods.
        Usage: transform [method] "Your text here"

        Available methods:
          - slug: Convert to URL-friendly slug
          - truncate: Truncate to 20 characters
          - snake: Convert to snake_case
          - camel: Convert to camelCase
          - title: Convert to Title Case
        """
        args = shlex.split(arg)
        if len(args) < 2:
            print('Usage: transform [method] "Your text here"')
            return

        method, text = args[0], args[1]

        try:
            print(f"\nTransforming text: {text}\n" + "-" * 40)

            if method == "slug":
                print(f"Slug: {slugify(text)}")
            elif method == "truncate":
                print(f"Truncated: {truncate(text, length=20)}")
            elif method == "snake":
                print(f"Snake Case: {to_snake_case(text)}")
            elif method == "camel":
                print(f"Camel Case: {to_camel_case(text)}")
            elif method == "title":
                print(f"Title Case: {to_title_case(text)}")
            else:
                print(f"Unknown method: {method}")
        except Exception as e:
            print(f"Error: {e}")

    def do_validate(self, arg: str) -> None:
        """
        Validate data based on specified type.
        Usage: validate [type] "data to validate"

        Available types:
          - email: Validate email address
          - url: Validate URL
          - date: Validate date (YYYY-MM-DD)
        """
        args = shlex.split(arg)
        if len(args) < 2:
            print('Usage: validate [type] "data to validate"')
            return

        data_type, data = args[0], args[1]

        try:
            print(f"\nValidating {data_type}: {data}\n" + "-" * 40)

            if data_type == "email":
                result = is_email(data)
                print(f"Is valid email: {result}")
            elif data_type == "url":
                result = is_url(data)
                print(f"Is valid URL: {result}")
            elif data_type == "date":
                result = is_date(data)
                print(f"Is valid date: {result}")
            else:
                print(f"Unknown validation type: {data_type}")
        except Exception as e:
            print(f"Error: {e}")

    def do_extract(self, arg: str) -> None:
        """
        Extract data from text.
        Usage: extract [type] "Your text here"

        Available types:
          - emails: Extract email addresses
        """
        args = shlex.split(arg)
        if len(args) < 2:
            print('Usage: extract [type] "Your text here"')
            return

        extract_type, text = args[0], args[1]

        try:
            print(f"\nExtracting from text: {text}\n" + "-" * 40)

            if extract_type == "emails":
                emails = extract_emails(text)
                if emails:
                    print("Emails found:")
                    for email in emails:
                        print(f"  - {email}")
                else:
                    print("No emails found.")
            else:
                print(f"Unknown extraction type: {extract_type}")
        except Exception as e:
            print(f"Error: {e}")

    def do_quit(self, arg: str) -> bool:
        """Exit the program."""
        print("Goodbye!")
        return True

    def do_exit(self, arg: str) -> bool:
        """Exit the program."""
        return self.do_quit(arg)

    def emptyline(self) -> None:
        """Handle empty line."""


def main() -> None:
    """Start the interactive shell."""
    Delta313Shell().cmdloop()


if __name__ == "__main__":
    main()
