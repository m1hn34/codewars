from o_or_e import odd_or_even

def test_basic():
    assert(odd_or_even([0]) == "even")

def test_medium():
    assert(odd_or_even([0, 1, 4]) == "odd")

def test_advanced():
    assert(odd_or_even([0, -1, -5]) == "even")

