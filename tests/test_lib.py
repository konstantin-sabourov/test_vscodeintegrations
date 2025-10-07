# Unit tests for lib/calc.py
from lib.calc import get_sum


# test sum of two integers
def test_get_sum_int():
    # two integers
    assert get_sum(1, 2) == 3


def test_get_sum_floats():
    # two floats
    assert get_sum(1.5, 2.6) == 4.1


def test_get_sum_int_and_float():
    # int and float
    assert get_sum(1, 2.5) == 3.5


def test_get_sum_nonnumeric():
    # not numeric
    pass
