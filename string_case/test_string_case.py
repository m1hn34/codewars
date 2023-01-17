# Python3
# Pytest script for string_case.py

from string_case import solve

def test_0():
    assert(solve('code') == 'code')
    assert(solve('CODe') == 'CODE')
    assert(solve('COde') == 'code')
    assert(solve('Code') == 'code')
