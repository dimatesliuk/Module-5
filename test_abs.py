import pytest

from calculator import abs

def test_abs_negative():
    result = abs(-10)
    assert result == 10

def test_abs_positive():
    result = abs(5)
    assert result == 5
