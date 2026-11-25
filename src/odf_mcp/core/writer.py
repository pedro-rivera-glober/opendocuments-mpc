from pathlib import Path
from typing import Self


class WriterDocument:
    """Handles creation and Markdown conversion for OpenDocument Text (.odt) files."""

    def __init__(self, filename: Path | str) -> None:
        """Initialize a WriterDocument bound to a target file path."""
        pass

    def create(self, text:str):
            with open(self.filename, 'w') as fl:
                fl.write(text)

    @classmethod
    def new_from_markdown(cls, filename: Path | str, markdown_text: str = "") -> Self:
        """Create or overwrite an .odt file from a Markdown string."""
        instance = cls(filename)
        instance.create(markdown_text)
        return instance

    @classmethod
    def to_markdown(cls, filename: Path | str) -> str:
        """Read an existing .odt file and return its content as Markdown.

        Raises:
            FileNotFoundError: If the target .odt file does not exist.
        """
        pass
