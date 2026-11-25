# tests/core/test_parser.py
import pytest
from odf_mcp.core.parser import parse_markdown


@pytest.mark.skip('non implemented yet')
def test_parse_writer_markdown(sample_writer_md: str):
    tokens = parse_markdown(sample_writer_md)
    token_types = [t.type for t in tokens]

    assert len(tokens) > 0
    assert "heading_open" in token_types
    assert "paragraph_open" in token_types
    assert "bullet_list_open" in token_types


@pytest.mark.skip('non implemented yet')
def test_parse_table_markdown(sample_calc_md: str):
    tokens = parse_markdown(sample_calc_md)
    token_types = [t.type for t in tokens]
    contents = [t.content for t in tokens if t.content]

    assert "table_open" in token_types
    assert "tr_open" in token_types
    assert "Name" in contents
    assert "Score" in contents


@pytest.mark.skip('non implemented yet')
def test_parse_impress_markdown(sample_impress_md: str):
    tokens = parse_markdown(sample_impress_md)
    token_types = [t.type for t in tokens]

    assert "hr" in token_types
    assert token_types.count("heading_open") == 2


@pytest.mark.skip('non implemented yet')
def test_parse_empty_string(empty_md: str):
    tokens = parse_markdown(empty_md)

    assert tokens == []
