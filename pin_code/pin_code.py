# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain 
# anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# eg:

# validate_pin("1234") == True
# validate_pin("12345") == False
# validate_pin("a234") == False

# my solution
# import re

# def validate_pin(pin):
#     regex_pattern4 = '\d{4}'
#     regex_pattern6 = '\d{6}'
#     result4 = re.match(regex_pattern4, pin)
#     result6 = re.match(regex_pattern6, pin)
#     if len(pin) == 4 and result4: return True
#     if len(pin) == 6 and result6: return True
#     else: return False

# simpler
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

# Function driver
print(validate_pin('12345a'))
