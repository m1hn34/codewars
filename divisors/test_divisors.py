# Python3
# PyTest for divisors.py

from divisors import divisors


def test_number_7():
    assert( divisors(7) == '7 is prime')

def test_number_12():
    assert( divisors(12) == [2, 3, 4, 6])
    
def test_number_13():
    assert( divisors(13) == '13 is prime')
    
def test_number_15():
    assert( divisors(15) == [3, 5])
    
def test_number_25():
    assert( divisors(25) == [5])
    
def test_number_31():
    assert( divisors(31) == '31 is prime')

def test_number_44():
    assert( divisors(44) == [2, 4, 11, 22])
