import pytest

from calculator import add



def test_add():
    result = add(3, 4)
    assert result == 8


def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)
