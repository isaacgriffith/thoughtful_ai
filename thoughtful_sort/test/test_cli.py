import pytest
from thoughtful_sort.cli import main
from unittest.mock import patch

def test_cli_standard_package(capsys):
    with patch('sys.argv', ['cli.py', '10', '10', '10', '10']):
        main()
        captured = capsys.readouterr()
        assert "Package category: STANDARD" in captured.out

def test_cli_special_bulky_volume(capsys):
    with patch('sys.argv', ['cli.py', '100', '100', '100', '10']):
        main()
        captured = capsys.readouterr()
        assert "Package category: SPECIAL" in captured.out

def test_cli_special_bulky_dimension(capsys):
    with patch('sys.argv', ['cli.py', '151', '10', '10', '10']):
        main()
        captured = capsys.readouterr()
        assert "Package category: SPECIAL" in captured.out

def test_cli_special_heavy(capsys):
    with patch('sys.argv', ['cli.py', '10', '10', '10', '21']):
        main()
        captured = capsys.readouterr()
        assert "Package category: SPECIAL" in captured.out

def test_cli_rejected_volume_and_heavy(capsys):
    with patch('sys.argv', ['cli.py', '100', '100', '100', '21']):
        main()
        captured = capsys.readouterr()
        assert "Package category: REJECTED" in captured.out

def test_cli_rejected_dimension_and_heavy(capsys):
    with patch('sys.argv', ['cli.py', '151', '10', '10', '21']):
        main()
        captured = capsys.readouterr()
        assert "Package category: REJECTED" in captured.out

def test_cli_negative_dimension(capsys):
    with patch('sys.argv', ['cli.py', '-1', '10', '10', '10']):
        main()
        captured = capsys.readouterr()
        assert "Error: All dimensions must be positive" in captured.out