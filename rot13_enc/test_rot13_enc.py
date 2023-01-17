# PyTest script for rot13_enc.py

from rot13_enc import rot13


def test_1():
    assert (rot13("test") == "grfg")


def test_2():
    assert (rot13("Test") == "Grfg")


def test_3():
    assert (rot13("Foo Bar 1+2 != 1+1") == "Sbb One 1+2 != 1+1")
