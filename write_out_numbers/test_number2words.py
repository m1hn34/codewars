# PyTest script for numbers.py

from number2words import write_out


def test_0():
    assert(write_out(0) == 'zero')


def test_1():
    assert(write_out(1) == 'one')


def test_2():
    assert(write_out(9) == 'nine')


def test_3():
    assert(write_out(10) == 'ten')


def test_4():
    assert(write_out(17) == 'seventeen')


def test_5():
    assert(write_out(20) == 'twenty')


def test_6():
    assert(write_out(21) == 'twenty-one')


def test_7():
    assert(write_out(45) == 'forty-five')


def test_8():
    assert(write_out(80) == 'eighty')


def test_9():
    assert(write_out(99) == 'ninety-nine')


def test_10():
    assert(write_out(100) == 'one hundred')


def test_11():
    assert(write_out(301) == 'three hundred one')


def test_12():
    assert(write_out(799) == 'seven hundred ninety-nine')


def test_13():
    assert(write_out(800) == 'eight hundred')


def test_14():
    assert(write_out(950) == 'nine hundred fifty')


def test_15():
    assert(write_out(1000) == 'one thousand')


def test_16():
    assert(write_out(1002) == 'one thousand two')


def test_17():
    assert(write_out(3051) == 'three thousand fifty-one')


def test_18():
    assert(write_out(7200) == 'seven thousand two hundred')


def test_19():
    assert(write_out(7219) == 'seven thousand two hundred nineteen')


def test_20():
    assert(write_out(8330) == 'eight thousand three hundred thirty')


def test_21():
    assert(write_out(99999) == 'ninety-nine thousand nine hundred ninety-nine')


def test_22():
    assert(write_out(888888) ==
           'eight hundred eighty-eight thousand eight hundred eighty-eight')
