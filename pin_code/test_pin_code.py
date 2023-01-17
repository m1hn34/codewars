# Python3
# Pytest script for pin_code.py

from pin_code import validate_pin

def test_0():
    assert(validate_pin('1') == False)

def test_1():
    assert(validate_pin('12') == False)

def test_2():
    assert(validate_pin('123') == False)

def test_3():
    assert(validate_pin('1234') == True)

def test_4():
    assert(validate_pin('12345') == False)

def test_5():
    assert(validate_pin('123456') == True)

def test_6():
    assert(validate_pin('1234567') == False)

def test_7():
    assert(validate_pin('1e') == False)

def test_8():
    assert(validate_pin('1-r') == False)

def test_9():
    assert(validate_pin('') == False)

def test_10():
    assert(validate_pin(' ') == False)

def test_11():
    assert(validate_pin('123 ') == False)

def test_12():
    assert(validate_pin('12345 ') == False)