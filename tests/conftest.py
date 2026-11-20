import os
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
    filename = 'dummy_file.odt'
    yield filename
    if os.path.exists(filename):
        os.remove(filename)