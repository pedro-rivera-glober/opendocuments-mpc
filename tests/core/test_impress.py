from pathlib import Path
import pytest
from odfdo import Document
from src.odf_mcp.core.impress import ImpressDocument


@pytest.mark.skip('non implemented yet')
def test_create_odp_from_markdown(odp_path: Path, sample_impress_md: str):
    ImpressDocument.new_from_markdown(odp_path, sample_impress_md)

    assert odp_path.exists()

    doc = Document(odp_path)
    pages = doc.body.get_draw_pages()
    assert len(pages) == 2

    slide_1_text = pages[0].text_recursive
    slide_2_text = pages[1].text_recursive

    assert "Slide 1" in slide_1_text
    assert "Opening slide content." in slide_1_text
    assert "Slide 2" in slide_2_text
    assert "Second slide content." in slide_2_text


@pytest.mark.skip('non implemented yet')
def test_overwrite_existing_odp(
    odp_path: Path,
    sample_impress_md: str,
    updated_impress_md: str,
):
    ImpressDocument.new_from_markdown(odp_path, sample_impress_md)
    ImpressDocument.new_from_markdown(odp_path, updated_impress_md)

    doc = Document(odp_path)
    pages = doc.body.get_draw_pages()
    assert len(pages) == 1

    slide_text = pages[0].text_recursive
    assert "Slide 1" not in slide_text
    assert "New Deck" in slide_text
    assert "Replaced slide content." in slide_text


@pytest.mark.skip('non implemented yet')
def test_odp_to_markdown(odp_path: Path, sample_impress_md: str):
    ImpressDocument.new_from_markdown(odp_path, sample_impress_md)

    md_output = ImpressDocument.to_markdown(odp_path)

    assert "# Slide 1" in md_output
    assert "Opening slide content." in md_output
    assert "---" in md_output
    assert "# Slide 2" in md_output
    assert "Second slide content." in md_output


@pytest.mark.skip('non implemented yet')
def test_odp_to_markdown_missing_file_raises(missing_odp_path: Path):
    with pytest.raises(FileNotFoundError):
        ImpressDocument.to_markdown(missing_odp_path)
