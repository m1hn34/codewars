# PyTest for persist.py

from persist import persistence


def test_0():
    assert(persistence(39) == 3)


def test_1():
    assert(persistence(4) == 0)


def test_2():
    assert(persistence(25) == 2)


def test_3():
    assert(persistence(999) == 4)
