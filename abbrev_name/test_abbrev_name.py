# Python3
# PyTest for abbrev_name.py

from abbrev_name import abbrevName

def test_name_Sam_Harris():
    assert( abbrevName('Sam Harris') == 'S.H')
    
def test_name_Samuel_Jackson():
    assert( abbrevName('Samuel Jackson') == 'S.J')

def test_name_Paul_Michael():
    assert( abbrevName('Paul Michael') == 'P.M')

def test_name_Adrian_Mutu():
    assert( abbrevName('Adrian Mutu') == 'A.M')
    
def test_name_Dirt_Rally():
    assert( abbrevName('Dirt Rally') == 'D.R')

def test_name_Elite_Dangerous():
    assert( abbrevName('Elite Dangerous') == 'E.D')
