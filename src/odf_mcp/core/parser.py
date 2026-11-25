from markdown_it.token import Token


def parse_markdown(text: str) -> list[Token]:
    """Parse a Markdown string into a list of markdown-it-py tokens.

    Args:
        text: Raw Markdown content (headings, paragraphs, lists, tables, or slide dividers).

    Returns:
        A list of Token objects representing the parsed Markdown AST.
    """
    pass
