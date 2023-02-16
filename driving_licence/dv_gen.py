'''
1-5: The first five characters of the surname (padded with 9s if less than 5 
characters)

6: The decade digit from the year of birth (e.g. for 1987 it would be 8)

7-8: The month of birth (7th character incremented by 5 if driver is female 
i.e. 51-62 instead of 01-12)

9-10: The date within the month of birth

11: The year digit from the year of birth (e.g. for 1987 it would be 7)

12-13: The first two initials of the first name and middle name, padded with a 
9 if no middle name

14: Arbitrary digit - usually 9, but decremented to differentiate drivers with 
the first 13 characters in common. We will always use 9

15-16: Two computer check digits. We will always use "AA"

=========
Code a UK driving license number using an Array of data.
The Array will look like this:

data = ["John","James","Smith","01-Jan-2000","M"]

========
Output the full 16 digit driving license number.

'''

# month number
from datetime import datetime
months = {
    "jan": "01",
    "january": "01",
    "feb": "02",
    "february": "02",
    "mar": "03",
    "march": "03",
    "apr": "04",
    "april": "04",
    "may": "05",
    "jun": "06",
    "june": "06",
    "jul": "07",
    "july": "07",
    "aug": "08",
    "august": "08",
    "sep": "09",
    "september": "09",
    "oct": "10",
    "october": "10",
    "nov": "11",
    "november": "11",
    "dec": "12",
    "december": "12"
}


# 1st Method long
def driver(data):
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


# 2nd Method short
def driver_2(data):
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


# Debug
print(driver(["John", "James", "Smith", "01-Jan-2000", "M"]))
print("SMITH001010JJ9AA")
