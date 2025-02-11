import pytest

from src.decorators import log, my_function


def test_log():
    assert log


def test_log_ok(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert '' in captured.out


def test_log_err():
    with pytest.raises(Exception):
        my_function(1, 'fff')
