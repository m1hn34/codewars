# PyTest script for welcome.py

from welcome import greet


def test_1():
    assert (greet('english') == 'Welcome')


def test_2():
    assert (greet('dutch') == 'Welkom')


def test_3():
    assert (greet('IP_ADDRESS_INVALID') == 'Welcome')


def test_4():
    assert (greet('') == 'Welcome')


def test_5():
    assert (greet(2) == 'Welcome')
