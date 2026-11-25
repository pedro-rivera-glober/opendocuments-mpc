from src.odf_mcp.core.writer import WriterDocument
from pathlib import Path
import pytest
from odfdo import Document


@pytest.mark.skip('non implemented yet')
def test_create_odt_from_markdown(odt_path: Path, sample_writer_md: str):
    WriterDocument.new_from_markdown(odt_path, sample_writer_md)

    assert odt_path.exists()

    doc = Document(odt_path)
    body = doc.body
    headers = [h.text_recursive for h in body.get_headers()]
    paragraphs = [p.text_recursive for p in body.get_paragraphs()]
    lists = body.get_lists()

    assert "This is a title" in headers
    assert "This is a subtitle" in headers
    assert "This is a text paragraph." in paragraphs
    assert len(lists) == 1
    assert len(lists[0].get_items()) == 3


@pytest.mark.skip('non implemented yet')
def test_overwrite_existing_odt(
    odt_path: Path,
    sample_writer_md: str,
    updated_writer_md: str,
):
    WriterDocument.new_from_markdown(odt_path, sample_writer_md)
    WriterDocument.new_from_markdown(odt_path, updated_writer_md)

    doc = Document(odt_path)
    body = doc.body
    headers = [h.text_recursive for h in body.get_headers()]
    paragraphs = [p.text_recursive for p in body.get_paragraphs()]

    assert "This is a title" not in headers
    assert "Updated Title" in headers
    assert "Completely replaced content." in paragraphs


@pytest.mark.skip('non implemented yet')
def test_odt_to_markdown(odt_path: Path, sample_writer_md: str):
    WriterDocument.new_from_markdown(odt_path, sample_writer_md)

    md_output = WriterDocument.to_markdown(odt_path)

    assert "# This is a title" in md_output
    assert "## This is a subtitle" in md_output
    assert "This is a text paragraph." in md_output
    assert "- Bullet item 1" in md_output
    assert "- Bullet item 2" in md_output
    assert "- Bullet item 3" in md_output


@pytest.mark.skip('non implemented yet')
def test_odt_to_markdown_missing_file_raises(missing_odt_path: Path):
    with pytest.raises(FileNotFoundError):
        WriterDocument.to_markdown(missing_odt_path)
