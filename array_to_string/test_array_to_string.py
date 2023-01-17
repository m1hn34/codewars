# Python3
# Pytest script for array_to_string.py

def test_0():
    assert(namelist([{'name': 'Bart'}, {'name': 'Lisa'},
                     {'name': 'Maggie'}]) == 'Bart, Lisa & Maggie')

def test_1():
    assert(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart & Lisa')

def test_2():
    assert(namelist([{'name': 'Bart'}]) == 'Bart')

def test_3():
    assert(namelist([]) == '')
