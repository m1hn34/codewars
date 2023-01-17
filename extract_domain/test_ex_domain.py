# PyTest script for extract.py

from ex_domain import domain_name


def test_1():
    assert (domain_name("http://google.com") == "google")


def test_2():
    assert (domain_name("http://google.co.jp") == "google")


def test_3():
    assert (domain_name("www.xakep.ru") == "xakep")


def test_4():
    assert (domain_name("https://youtube.com") == "youtube")


def test_5():
    assert (domain_name("google.com") == "google")
