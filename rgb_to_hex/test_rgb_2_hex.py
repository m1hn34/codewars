# PyTest script for rg_to_text

from rgb_2_hex import rgb


def test_1():
    assert (rgb(255, 255, 255) == 'FFFFFF')


def test_2():
    assert (rgb(255, 255, 300) == 'FFFFFF')


def test_3():
    assert (rgb(0, 0, 0) == '000000')


def test_4():
    assert (rgb(148, 0, 211) == '9400D3')


def test_5():
    assert (rgb(-20, 275, 125) == '00FF7D')
