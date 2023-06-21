# PyTest script for vowel_code.py

from vowel_code import encode, decode


def test_1():
    a = "hello"
    b = "h2ll4"
    assert (encode(a) == b)


def test_2():
    a = "How are you today?"
    b = "H4w 1r2 y45 t4d1y?"
    assert (encode(a) == b)


def test_3():
    a = "This is an encoding test."
    b = "Th3s 3s 1n 2nc4d3ng t2st."
    assert (encode(a) == b)


def test_4():
    a = "h2ll4"
    b = "hello"
    assert (decode(a) == b)
