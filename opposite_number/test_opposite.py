# Python3
# Pytest script for opposite.py

from opposite import opposite

def test_0():
    assert(opposite(1) == -1)
    assert(opposite(-2) == 2)
    assert(opposite(33) == -33)
    assert(opposite(-69) == 69)

