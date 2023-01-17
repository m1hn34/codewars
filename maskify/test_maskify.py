from maskify import maskify


# Python3
# PyTest for maskify.py


def test_0():
    assert(maskify('') == '')


def test_1():
    assert(maskify('123') == '123')


def test_2():
    assert(maskify('SF$SDfgsd2eA') == '########d2eA')
