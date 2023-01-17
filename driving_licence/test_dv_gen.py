# test script for dv_ge.py

from dv_gen import driver


def test_0():
    assert(driver(["John", "James", "Smith", "01-Jan-2000", "M"])
           == "SMITH001010JJ9AA")


def test_1():
    assert(driver(["Johanna", "", "Gibbs", "13-Dec-1981", "F"])
           == "GIBBS862131J99AA")


def test_2():
    assert(driver(["Andrew", "Robert", "Lee",
           "02-September-1981", "M"]) == "LEE99809021AR9AA")
