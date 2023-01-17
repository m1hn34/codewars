# PyTest script for anagram.py

from anagram import is_anagram


def test_1():
    assert (is_anagram("foefet", "toffee") == True)


def test_2():
    assert (is_anagram("Buckethead", "DeathCubeK") == True)


def test_3():
    assert (is_anagram("Twoo", "WooT") == True)


def test_4():
    assert (is_anagram("dumble", "bumble") == False)


def test_5():
    assert (is_anagram("ound", "round") == False)


def test_6():
    assert (is_anagram("apple", "pale") == False)
