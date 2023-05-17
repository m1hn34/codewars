# PyTest script for occurrences.py

from occurrences import delete_nth


def test_1():
    a1 = [20, 37, 20, 21]
    a2 = 1
    b = [20, 37, 21]
    assert (delete_nth(a1, a2) == b)


def test_2():
    a1 = [1, 1, 3, 3, 7, 2, 2, 2, 2]
    a2 = 3
    b = [1, 1, 3, 3, 7, 2, 2, 2]
    assert (delete_nth(a1, a2) == b)
