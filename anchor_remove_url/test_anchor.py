# PyTest for anchor.py

from anchor import remove_url_anchor


def test_1():
    assert (remove_url_anchor("www.codewars.com#about") == "www.codewars.com")


def test_2():
    assert (remove_url_anchor("www.codewars.com/katas/?page=1#about")
            == "www.codewars.com/katas/?page=1")


def test_3():
    assert (remove_url_anchor("www.codewars.com/katas/")
            == "www.codewars.com/katas/")
