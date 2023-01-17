# PyTest for sum_the_strings

from sum_string import sum_str


def test_1():
    assert (sum_str('4', '5') == '9')


def test_2():
    assert (sum_str('34', '5') == '39')


def test_3():
    assert (sum_str('', '') == '0')


def test_4():
    assert (sum_str('2', '') == '2')


def test_5():
    assert (sum_str('-5', '3') == '-2')
