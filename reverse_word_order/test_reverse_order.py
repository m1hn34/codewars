# PyTest for reverse_order.py

from reverse_order import reverse


def test_1():
    a = "Hello World"
    b = "World Hello"
    assert (reverse(a) == b)


def test_2():
    a = "Hi There!"
    b = "There! Hi"
    assert (reverse(a) == b)


def test_3():
    a = "Foo Bar "
    b = "Bar Foo"
    assert (reverse(a) == b)


def test_4():
    a = "ojs hh r pjgwyieirlrhwpelyhklpy typsq isktrkhguwolifpfggpirsfieh ky sow uyawfp  trskffegf ky"
    b = "ky trskffegf  uyawfp sow ky isktrkhguwolifpfggpirsfieh typsq pjgwyieirlrhwpelyhklpy r hh ojs"
    assert (reverse(a) == b)
