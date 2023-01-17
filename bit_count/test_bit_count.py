# Python3
# PyTest for bit_count.py

from bit_count import countBits
from bit_count import countStrBits

# Test


def test_0():
    assert(countBits(0) == 0)


def test_4():
    assert(countBits(4) == 1)


def test_7():
    assert(countBits(7) == 3)


def test_9():
    assert(countBits(9) == 2)


def test_10():
    assert(countBits(10) == 2)


def test_55():
    assert(countBits(55) == 5)


def test_33():
    assert(countBits(33) == 2)


def test_66():
    assert(countBits(66) == 2)


def test_99():
    assert(countBits(99) == 4)


def test_1889():
    assert(countBits(1889) == 6)


def test_3306():
    assert(countBits(3306) == 7)


def test_hello_world():
    assert(countStrBits('hello world') ==
           '1101000 1100101 1101100 1101100 1101111 100000 1110111 1101111 1110010 1101100 1100100')


def test_mihnea():
    assert(countStrBits('mihnea') ==
           '1101101 1101001 1101000 1101110 1100101 1100001')
