# PyTest for isograms.py

from isograms import is_isogram


def test_0():
    assert(is_isogram('Dermatoglyphics') == True)


def test_1():
    assert(is_isogram('isogram') == True)


def test_2():
    assert(is_isogram('aba') == False)


def test_3():
    assert(is_isogram('moOse') == False)


def test_4():
    assert(is_isogram('isIsogram') == False)


def test_5():
    assert(is_isogram('') == True)
