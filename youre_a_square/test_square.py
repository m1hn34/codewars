# Pytest for square.py

from square import is_square


def test_0():
    assert(is_square(-1) == False)
    assert(is_square(0) == True)
    assert(is_square(3) == False)
    assert(is_square(4) == True)
    assert(is_square(25) == True)
    assert(is_square(26) == False)
