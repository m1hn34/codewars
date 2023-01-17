# PyTest script for max_sub.py

from max_sub import max_sequence


def test_0():
    assert(max_sequence([]) == 0)


def test_1():
    assert(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)


def test_2():
    assert(max_sequence([1, 2, 3]) == 6)
