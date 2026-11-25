from pathlib import Path
import pytest


@pytest.fixture
def empty_md() -> str:
    return ""

# WRITER

@pytest.fixture
def odt_path(tmp_path: Path) -> Path:
    return tmp_path / "test_doc.odt"


@pytest.fixture
def missing_odt_path(tmp_path: Path) -> Path:
    return tmp_path / "does_not_exist.odt"


@pytest.fixture
def sample_writer_md() -> str:
    return "\n".join((
        "# This is a title",
        "## This is a subtitle",
        "This is a text paragraph.",
        "- Bullet item 1",
        "- Bullet item 2",
        "- Bullet item 3",
    ))


@pytest.fixture
def updated_writer_md() -> str:
    return "\n".join((
        "# Updated Title",
        "Completely replaced content.",
    ))


# CALC

@pytest.fixture
def ods_path(tmp_path: Path) -> Path:
    return tmp_path / "test_sheet.ods"


@pytest.fixture
def missing_ods_path(tmp_path: Path) -> Path:
    return tmp_path / "does_not_exist.ods"


@pytest.fixture
def sample_calc_md() -> str:
    return "\n".join((
        "| Name | Score |",
        "| ---- | ----- |",
        "| A    | 1     |",
        "| B    | 2     |",
    ))


@pytest.fixture
def updated_calc_md() -> str:
    return "\n".join((
        "| Item  | Qty |",
        "| ----- | --- |",
        "| Apple | 10  |",
    ))


# IMPRESS

@pytest.fixture
def updated_impress_md() -> str:
    return "\n".join((
        "# New Deck",
        "Replaced slide content.",
    ))


@pytest.fixture
def sample_impress_md() -> str:
    return "\n".join((
        "# Slide 1",
        "Opening slide content.",
        "---",
        "# Slide 2",
        "Second slide content.",
    ))


@pytest.fixture
def missing_odp_path(tmp_path: Path) -> Path:
    return tmp_path / "does_not_exist.odp"


@pytest.fixture
def odp_path(tmp_path: Path) -> Path:
    return tmp_path / "test_deck.odp"
