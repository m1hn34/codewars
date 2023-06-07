# PyTest script for coupon.py

from coupon import check_coupon


def test_1():
    entered_code = "123"
    correct_code = "123"
    current_date = "July 9, 2015"
    expiration_date = "July 9, 2015"
    result = True
    assert (check_coupon(entered_code, correct_code,
            current_date, expiration_date) == result)


def test_2():
    entered_code = "123"
    correct_code = "123"
    current_date = "July 9, 2015"
    expiration_date = "July 2, 2015"
    result = False
    assert (check_coupon(entered_code, correct_code,
            current_date, expiration_date) == result)


def test_3():
    entered_code = "111"
    correct_code = "222"
    current_date = "September 5, 2000"
    expiration_date = "September 5, 2000"
    result = False
    assert (check_coupon(entered_code, correct_code,
            current_date, expiration_date) == result)


def test_4():
    entered_code = "123"
    correct_code = "123"
    current_date = "September 4, 2014"
    expiration_date = "September 5, 2014"
    result = True
    assert (check_coupon(entered_code, correct_code,
            current_date, expiration_date) == result)
