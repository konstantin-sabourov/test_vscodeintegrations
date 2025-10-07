# Unit tests for lib/calc.py
import pytest
from lib.calc import get_sum


# test sum of two integers
def test_get_sum_int():
    # two integers
    assert get_sum(1, 2) == 3


def test_get_sum_floats():
    # two floats
    # Using approximate equality for floating point comparison
    result = get_sum(1.5, 2.6)
    assert abs(result - 4.1) < 1e-10


def test_get_sum_int_and_float():
    # int and float
    assert get_sum(1, 2.5) == pytest.approx(3.5)


def test_get_sum_negative_numbers():
    # negative numbers
    assert get_sum(-1, -2) == -3
    assert get_sum(-1, 2) == 1
    assert get_sum(1, -2) == -1


def test_get_sum_with_zero():
    # zero values
    assert get_sum(0, 5) == 5
    assert get_sum(0, 0) == 0
    assert get_sum(-5, 0) == -5


def test_get_sum_large_numbers():
    # large numbers
    assert get_sum(1000000, 2000000) == 3000000


def test_get_sum_nonnumeric_first_arg():
    # not numeric - first argument
    with pytest.raises(TypeError):
        get_sum("a", 2)
    with pytest.raises(TypeError):
        get_sum(None, 2)
    with pytest.raises(TypeError):
        get_sum([], 2)


def test_get_sum_nonnumeric_second_arg():
    # not numeric - second argument
    with pytest.raises(TypeError):
        get_sum(2, "b")
    with pytest.raises(TypeError):
        get_sum(2, None)
    with pytest.raises(TypeError):
        get_sum(2, [])


def test_get_sum_both_nonnumeric():
    # both arguments non-numeric
    with pytest.raises(TypeError):
        get_sum("a", "b")
