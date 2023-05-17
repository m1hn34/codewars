# PyTest script for perfect_square.py


from perfect_square import is_square


def test_1():
    a = -1
    b = False
    assert (is_square(a) == b)


def test_2():
    a = 0
    b = True
    assert (is_square(a) == b)


def test_3():
    a = 3
    b = False
    assert (is_square(a) == b)


def test_4():
    a = 4
    b = True
    assert (is_square(a) == b)


def test_5():
    a = 25
    b = True
    assert (is_square(a) == b)


def test_6():
    a = 26
    b = False
    assert (is_square(a) == b)


