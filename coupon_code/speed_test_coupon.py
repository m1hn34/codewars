# Speed test script for coupon.py

import timeit

import_module = "import random"

test_code_1 = '''
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
'''

print("test_code_1:")
print(timeit.repeat(stmt=test_code_1, setup=import_module))
