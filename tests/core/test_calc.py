from pathlib import Path
import pytest
from odfdo import Document
from src.odf_mcp.core.calc import CalcDocument


@pytest.mark.skip('non implemented yet')
def test_create_ods_from_markdown(ods_path: Path, sample_calc_md: str):
    CalcDocument.new_from_markdown(ods_path, sample_calc_md)

    assert ods_path.exists()

    doc = Document(ods_path)
    tables = doc.body.get_tables()
    assert len(tables) == 1

    rows = [[str(cell) for cell in row] for row in tables[0].get_values()]
    assert rows == [
        ["Name", "Score"],
        ["A", "1"],
        ["B", "2"],
    ]


@pytest.mark.skip('non implemented yet')
def test_overwrite_existing_ods(
    ods_path: Path,
    sample_calc_md: str,
    updated_calc_md: str,
):
    CalcDocument.new_from_markdown(ods_path, sample_calc_md)
    CalcDocument.new_from_markdown(ods_path, updated_calc_md)

    doc = Document(ods_path)
    tables = doc.body.get_tables()
    rows = [[str(cell) for cell in row] for row in tables[0].get_values()]

    assert rows == [
        ["Item", "Qty"],
        ["Apple", "10"],
    ]


@pytest.mark.skip('non implemented yet')
def test_ods_to_markdown(ods_path: Path, sample_calc_md: str):
    CalcDocument.new_from_markdown(ods_path, sample_calc_md)

    md_output = CalcDocument.to_markdown(ods_path)

    assert "Name" in md_output
    assert "Score" in md_output
    assert "A" in md_output
    assert "B" in md_output
    assert "|" in md_output


@pytest.mark.skip('non implemented yet')
def test_ods_to_markdown_missing_file_raises(missing_ods_path: Path):
    with pytest.raises(FileNotFoundError):
        CalcDocument.to_markdown(missing_ods_path)
