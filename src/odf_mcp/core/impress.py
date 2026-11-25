from pathlib import Path
from typing import Self


class ImpressDocument:
    """Handles creation and Markdown conversion for OpenDocument Presentation (.odp) files."""

    def __init__(self, filename: Path | str) -> None:
        """Initialize an ImpressDocument bound to a target file path."""
        pass

    @classmethod
    def new_from_markdown(cls, filename: Path | str, markdown_text: str = "") -> Self:
        """Create or overwrite an .odp file from a Markdown string split by slide dividers."""
        pass

    @classmethod
    def to_markdown(cls, filename: Path | str) -> str:
        """Read an existing .odp file and return its slides as Markdown separated by '---'.

        Raises:
            FileNotFoundError: If the target .odp file does not exist.
        """
        pass
