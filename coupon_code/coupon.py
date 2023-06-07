'''
Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid 
and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will 
be passed as strings in this format: "MONTH DATE, YEAR".

Examples:
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False

!!! WARNING !!!:
The random tests of this kata have an issue where the enetered_code and
correct_code values are of different data types, i.e.: 2(int) != '2'(str).

For a 7kyu kata I would expect a heads-up regarding the discrepancies between 
data types.

This is my final method. I am done with this kata.
'''

from datetime import datetime

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

# 1st method


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if str(entered_code) != str(correct_code):
        return False

    else:
        c_month = current_date.split(" ")[0]
        c_day = current_date.split(" ")[1].strip(",")
        c_year = current_date.split(" ")[2]
        e_month = expiration_date.split(" ")[0]
        e_day = expiration_date.split(" ")[1].strip(",")
        e_year = expiration_date.split(" ")[2]

        now = datetime(int(c_year), months.get(c_month), int(c_day)).date()
        coupon = datetime(int(e_year), months.get(e_month), int(e_day)).date()

    return coupon >= now


# debug
print(check_coupon('123', '123', 'September 25, 2014', 'September 5, 2014'))
print(False)
