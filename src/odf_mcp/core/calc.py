from pathlib import Path
from typing import Self


class CalcDocument:
    """Handles creation and Markdown conversion for OpenDocument Spreadsheet (.ods) files."""

    def __init__(self, filename: Path | str) -> None:
        """Initialize a CalcDocument bound to a target file path."""
        pass

    @classmethod
    def new_from_markdown(cls, filename: Path | str, markdown_text: str = "") -> Self:
        """Create or overwrite an .ods file from a Markdown table string."""
        pass

    @classmethod
    def to_markdown(cls, filename: Path | str) -> str:
        """Read an existing .ods file and return its first sheet as a Markdown table.

        Raises:
            FileNotFoundError: If the target .ods file does not exist.
        """
        pass
