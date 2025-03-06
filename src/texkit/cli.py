"""Command-line interface for text utilities."""

import sys

import click  # type: ignore[import-not-found]
from rich.console import Console  # type: ignore[import-not-found]
from rich.table import Table  # type: ignore[import-not-found]

from texkit import analyzer, transformer
from texkit.advanced import summarizer

console = Console()


@click.group()
@click.version_option()
def cli() -> None:
    """Text Utilities - A collection of text processing tools."""


@cli.command()
@click.argument("text", required=False)
@click.option("--file", "-f", type=click.File("r"), help="Input file")
@click.option("--top", "-n", default=10, help="Number of top words to show")
def analyze(text: str | None, file: click.File | None, top: int) -> None:
    """Analyze text and show statistics."""
    if file:
        content = file.read()
    elif text:
        content = text
    else:
        content = sys.stdin.read()

    if not content.strip():
        console.print("[bold red]Error:[/] No text provided")
        return

    # Create rich table for results
    table = Table(title="Text Analysis Results")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    # Add basic metrics
    word_count = len(content.split())
    table.add_row("Word Count", str(word_count))
    table.add_row("Character Count", str(len(content)))
    table.add_row("Sentence Count", str(analyzer.sentence_count(content)))
    table.add_row(
        "Average Word Length", f"{analyzer.average_word_length(content):.2f}"
    )

    # Show top words
    console.print(table)

    top_words = analyzer.get_top_words(content, n=top)
    if top_words:
        word_table = Table(title=f"Top {top} Words")
        word_table.add_column("Word", style="blue")
        word_table.add_column("Frequency", style="magenta")

        for word, freq in top_words:
            word_table.add_row(word, str(freq))

        console.print(word_table)


@cli.command()
@click.argument("text", required=False)
@click.option("--file", "-f", type=click.File("r"), help="Input file")
@click.option("--slugify", "-s", is_flag=True, help="Convert to slug format")
@click.option("--truncate", "-t", type=int, help="Truncate to length")
def transform(
    text: str | None,
    file: click.File | None,
    slugify: bool,
    truncate: int | None,
) -> None:
    """Transform text with various operations."""
    if file:
        content = file.read()
    elif text:
        content = text
    else:
        content = sys.stdin.read()

    if not content.strip():
        console.print("[bold red]Error:[/] No text provided")
        return

    result = content

    if slugify:
        result = transformer.slugify(result)

    if truncate:
        result = transformer.truncate(result, length=truncate)

    console.print(result)


@cli.command()
@click.argument("text", required=False)
@click.option("--file", "-f", type=click.File("r"), help="Input file")
@click.option("--sentences", "-s", default=3, help="Number of sentences")
def summarize(
    text: str | None, file: click.File | None, sentences: int
) -> None:
    """Create a summary of the text."""
    if file:
        content = file.read()
    elif text:
        content = text
    else:
        content = sys.stdin.read()

    if not content.strip():
        console.print("[bold red]Error:[/] No text provided")
        return

    summary = summarizer.summarize(content, sentence_count=sentences)
    readability = summarizer.calculate_readability(content)

    console.print("[bold green]Summary:[/]")
    console.print(summary)
    console.print("\n[bold green]Readability Metrics:[/]")

    for metric, value in readability.items():
        console.print(f"{metric}: {value}")


def main() -> None:
    """Main entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
