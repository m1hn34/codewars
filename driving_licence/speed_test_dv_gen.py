# Timeit test script for dv_gen.py

import timeit

import_module = "import random"

test_code_1 = '''
def driver_1(data):
    dv_code = ""

    # surname - 5
    if len(data[2]) < 5:
        dv_code += data[2] + ((5 - len(data[2])) * '9')
    else:
        dv_code += data[2][0:5]

    # decade - 6
    dv_code += data[3][-2]

    # month - 7-8
    if data[4] == 'F':
        dv_code += months[data[3][3:6].lower()]
        s = list(dv_code)
        s[-2] = str(int(s[-2]) + 5)
        dv_code = ''.join(s)
    else:
        dv_code += months[data[3][3:6].lower()]

    # day - 9-10
    dv_code += data[3][0:2]

    # year digit - 11
    dv_code += data[3][-1]

    # first and middle name initials - 12-13
    if data[1]:
        dv_code += data[0][0] + data[1][0]
    else:
        dv_code += data[0][0] + '9'

    # arbitrary digit (9) - 14
    dv_code += '9'

    # computer check digit (AA) - 15-16
    dv_code += 'AA'

    return dv_code.upper()
'''

test_code_2 = '''
def driver(data):
    first, middle, last, dob, gender = data
    try:
        d = datetime.strptime(dob, '%d-%b-%Y')
    except ValueError:
        d = datetime.strptime(dob, '%d-%B-%Y')

    return '{:9<5}{[2]}{:0>2}{:0>2}{[3]}{[0]}{[0]}9AA'.format(
        last[:5].upper(),
        str(d.year),
        d.month + (50 if gender == 'F' else 0),
        d.day,
        str(d.year),
        first,
        middle if middle else '9')
'''

print("Method 1")
print(timeit.repeat(stmt=test_code_1, setup=import_module))

print("Method 2")
print(timeit.repeat(stmt=test_code_2, setup=import_module))
