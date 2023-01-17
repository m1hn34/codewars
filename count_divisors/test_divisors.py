# PyTest script for divisors.py

from divisors import divisors


def test_1():
    assert (divisors(1) == 1)


def test_2():
    assert (divisors(4) == 3)


def test_3():
    assert (divisors(5) == 2)


def test_4():
    assert (divisors(12) == 6)


def test_5():
    assert (divisors(30) == 8)


def test_6():
    assert (divisors(4096) == 13)
