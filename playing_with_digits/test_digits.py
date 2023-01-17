# PyTest script for digits.py

'''
def sample_tests():
        test.assert_equals(dig_pow(89, 1), 1)
        test.assert_equals(dig_pow(92, 1), -1)
        test.assert_equals(dig_pow(46288, 3), 51)
'''

from digits import dig_pow


def test_1():
    assert (dig_pow(89, 1) == 1)


def test_2():
    assert (dig_pow(92, 1) == -1)


def test_3():
    assert (dig_pow(46288, 3) == 51)
