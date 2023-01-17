# Python3
# Pytest script or parse_int.py

from parse_int import parse_int



def test_0():
    assert(parse_int('one') == 1)
    assert(parse_int('twenty') == 20)
    assert(parse_int('two hundred forty-six') == 246)
    
