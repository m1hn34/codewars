# PyTest script for word.py


from word import high


def test_1():
    a = 'man i need a taxi up to ubud'
    b = 'taxi'
    assert (high(a) == b)


def test_2():
    a = 'what time are we climbing up the volcano'
    b = 'volcano'
    assert (high(a) == b)


def test_3():
    a = 'take me to semynak'
    b = 'semynak'
    assert (high(a) == b)


def test_4():
    a = 'aa b'
    b = 'aa'
    assert (high(a) == b)


def test_5():
    a = 'b aa'
    b = 'b'
    assert (high(a) == b)


def test_6():
    a = 'bb d'
    b = 'bb'
    assert (high(a) == b)


def test_7():
    a = 'd bb'
    b = 'd'
    assert (high(a) == b)


def test_8():
    a = "aaa b"
    b = "aaa"
    assert (high(a) == b)
