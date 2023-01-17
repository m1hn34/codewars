# PyTest for array_diff.py

from array_diff import array_diff


def test_0():
    assert(array_diff([1, 2], [1]) == [2])


def test_1():
    assert(array_diff([1, 2, 2], [1]) == [2, 2])


def test_2():
    assert(array_diff([1, 2, 2], [2]) == [1])


def test_3():
    assert(array_diff([1, 2, 2], []) == [1, 2, 2])


def test_4():
    assert(array_diff([], [1, 2]) == [])


def test_5():
    assert(array_diff([1, 2, 3], [1, 2]) == [3])
