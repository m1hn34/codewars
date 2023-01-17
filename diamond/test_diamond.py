# PyTest script for diamond.py

from diamond import diamond


def test_1():
    assert (diamond(1) == "*\n")


def test_2():
    assert (diamond(2) == None)


def test_3():
    assert (diamond(3) == " *\n***\n *\n")


def test_4():
    assert (diamond(4) == None)


def test_5():
    assert (diamond(5) == "  *\n ***\n*****\n ***\n  *\n")


def test_6():
    assert (diamond(0) == None)


def test_7():
    assert (diamond(-3) == None)
