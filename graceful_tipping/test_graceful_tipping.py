# Python3
# Test for the graceful_tipping.py

from graceful_tipping import graceful_tipping

def basic_tests():
    assert(graceful_tipping(1) == 2)
    assert(graceful_tipping(7) == 9)
    assert(graceful_tipping(12) == 15)
    assert(graceful_tipping(86) == 100)
    assert(graceful_tipping(99) == 150)
    assert(graceful_tipping(1149) == 1500)
    assert(graceful_tipping(983212) == 1500000)
