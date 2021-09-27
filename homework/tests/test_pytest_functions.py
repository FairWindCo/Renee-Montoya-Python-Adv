import pytest as pytest

from functions_to_test import Calculator


def test_substract():
    assert Calculator().subtract(2, 1) == 1


def test_sum():
    assert Calculator().add(2, 1) == 3


def test_multiply():
    assert Calculator().multiply(2, 1) == 2


def test_divide():
    assert Calculator().divide(2, 1) == 2


def test_divide_zero():
    with pytest.raises(ValueError):
        Calculator().divide(2, 0)
