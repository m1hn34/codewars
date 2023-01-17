from string_to_number import toNumber

def test_basic():
    num = "1234"
    assert(toNumber(num) == 1234)

def test_medium():
    num = "605"
    assert(toNumber(num) == 605)

def test_advanced():
    num = "1405"
    assert(toNumber(num) == 1405)

def test_impossible():
    num = "-7"
    assert(toNumber(num) == -7)

