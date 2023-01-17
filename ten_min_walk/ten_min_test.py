# Python test script for ten_min_walk.py
from ten_min import is_valid_walk


def test_0():
    assert(is_valid_walk(['n', 's', 'n', 's', 'n',
           's', 'n', 's', 'n', 's']) == True)


def test_1():
    assert(is_valid_walk(['w', 'e', 'w', 'e', 'w',
           'e', 'w', 'e', 'w', 'e', 'w', 'e']) == False)


def test_2():
    assert(is_valid_walk(['w']) == False)


def test_3():
    assert(is_valid_walk(['n', 'n', 'n', 's', 'n',
           's', 'n', 's', 'n', 's']) == False)
