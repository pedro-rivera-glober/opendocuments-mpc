import pytest


@pytest.fixture
def dummy_markdown_text():
    return '\n'.join((
        '# this is a title',
        '## this is a subtitle',
        'this is a text paragraph',
        '- this is a bullet list element',
        '- this is a bullet list element',
        '- this is a bullet list element',
    ))


@pytest.fixture
def dummy_odt_filename():
    return 'dummy_file.odt'