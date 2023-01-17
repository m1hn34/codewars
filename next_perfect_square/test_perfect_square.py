# PyTest for perfect_square.py

from perfect_square import find_next_square


def test_0():
    assert(find_next_square(121) == 144)


def test_1():
    assert(find_next_square(625) == 676)


def test_2():
    assert(find_next_square(319225) == 320356)


def test_3():
    assert(find_next_square(15241383936) == 15241630849)
