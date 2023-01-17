# Python3
# PyTest for pw_cracker.py

from pw_cracker import password_cracker


def test_e6fb06210fafc02fd7479ddbed2d042cc3a5155e():
    assert(password_cracker('e6fb06210fafc02fd7479ddbed2d042cc3a5155e') == 'code')


def test_a94a8fe5ccb19ba61c4c0873d391e987982fbbd3():
    assert(password_cracker('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3') == 'test')

def test_
