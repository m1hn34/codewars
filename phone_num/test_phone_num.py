# Python3
# Unittest for phone_num.py

from phone_num import create_phone_number

def test_num_1():
    assert(create_phone_number(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890")

def test_num_2():
    assert(create_phone_number(
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111")
    
def test_num_3():
    assert(create_phone_number(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890")
    
def test_num_4():
    assert(create_phone_number(
        [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890")
    
def test_num_5():
    assert(create_phone_number(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000")
    
def test_num_6():
    assert(create_phone_number(
        [0, 7, 3, 0, 7, 3, 0, 7, 3, 7]) == "(073) 073-0737")
    

