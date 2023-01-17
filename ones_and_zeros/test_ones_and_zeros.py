# Python3.9
# PyTest for ones_and_zeros.py

from ones_and_zeros import binary_array_to_number

# Test


def test_0():
    assert(binary_array_to_number([0, 0, 0, 0]) == 0)


def test_1():
    assert(binary_array_to_number([0, 0, 0, 1]) == 1)


def test_2():
    assert(binary_array_to_number([0, 0, 1, 0]) == 2)


def test_3():
    assert(binary_array_to_number([0, 0, 1, 1]) == 3)


def test_4():
    assert(binary_array_to_number([0, 1, 0, 0]) == 4)


def test_5():
    assert(binary_array_to_number([0, 1, 0, 1]) == 5)


def test_6():
    assert(binary_array_to_number([0, 1, 1, 0]) == 6)


def test_7():
    assert(binary_array_to_number([0, 1, 1, 1]) == 7)


def test_8():
    assert(binary_array_to_number([1, 0, 0, 0]) == 8)


def test_9():
    assert(binary_array_to_number([1, 0, 0, 1]) == 9)


def test_10():
    assert(binary_array_to_number([1, 0, 1, 0]) == 10)


def test_11():
    assert(binary_array_to_number([1, 0, 1, 1]) == 11)


def test_12():
    assert(binary_array_to_number([1, 1, 0, 0]) == 12)


def test_13():
    assert(binary_array_to_number([1, 1, 0, 1]) == 13)


def test_14():
    assert(binary_array_to_number([1, 1, 1, 0]) == 14)


def test_15():
    assert(binary_array_to_number([1, 1, 1, 1]) == 15)
