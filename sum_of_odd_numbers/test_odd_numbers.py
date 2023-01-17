# pytest script for odd_numbers.py

from odd_numbers import row_sum_odd_numbers


def test_0():
    assert (row_sum_odd_numbers(1) == 1)


def test_1():
    assert (row_sum_odd_numbers(2) == 8)


def test_2():
    assert (row_sum_odd_numbers(13) == 2197)


def test_3():
    assert (row_sum_odd_numbers(19) == 6859)


def test_4():
    assert (row_sum_odd_numbers(41) == 68921)
