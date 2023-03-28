from unittest.mock import mock_open, patch
import pytest
from src.pre_built.counter import count_ocurrences

EXPECTED_RESULT_PYTHON = 2
EXPECTED_RESULT_JAVASCRIP = 3


@pytest.fixture
def fake_content():
    fake_text = """
    Python javascript java, pthon, JavaScript,
    typescrypt pyThon javaSCRIPT
    """
    return fake_text


def test_counter(fake_content):
    with patch("builtins.open", mock_open(read_data=fake_content)):
        occurrences_of_python = count_ocurrences("data/jobs.csv", "Python")
        assert occurrences_of_python == EXPECTED_RESULT_PYTHON

    with patch("builtins.open", mock_open(read_data=fake_content)):
        occurrences_of_javascript = count_ocurrences(
            "data/jobs.csv", "Javascript"
        )
        assert occurrences_of_javascript == EXPECTED_RESULT_JAVASCRIP
