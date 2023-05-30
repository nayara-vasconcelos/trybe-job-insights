import pytest
from src.pre_built.brazilian_jobs import read_brazilian_file
from unittest.mock import mock_open, patch


def test_brazilian_jobs():
    mock_data = (
        "titulo,salario,tipo\n"
        + "Maquinista,2000,trainee\n"
        + "Motorista,3000,full time"
    )

    expected_output = [
        {"title": "Maquinista", "salary": "2000", "type": "trainee"},
        {"title": "Motorista", "salary": "3000", "type": "full time"},
    ]

    with pytest.raises(ValueError, match="Invalid file format"):
        read_brazilian_file("any_file_path.json")

    with patch("builtins.open", mock_open(read_data=mock_data)):
        assert read_brazilian_file("any_file_path.csv") == expected_output
