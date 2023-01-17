# Python3
# Pytest script for char_count.py

from char_count import count

def test_0():
    assert(count('aba') == {'a': 2, 'b': 1})

def test_1():
    assert(count('') == {})

def test_2():
    assert(count('Abba') == {'b': 2, 'A': 1, 'a': 1})
