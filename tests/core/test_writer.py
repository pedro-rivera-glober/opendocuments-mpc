import os
from src.odf_mcp.core.writer import WriterDocument


def test_odt_generator(dummy_odt_filename, dummy_markdown_text):
    doc = WriterDocument.new_from_markdown(dummy_odt_filename, dummy_markdown_text)
    assert doc is not None
    assert os.path.exists(dummy_odt_filename)