# PyTest

from pangram import is_pangram


def test_1():
    assert (is_pangram("The quick, brown fox jumps over the lazy dog!") == True)


def test_2():
    assert (is_pangram("1bcdefghijklmnopqrstuvwxyz") == False)
