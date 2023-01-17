# Complete the function that accepts a string parameter, and reversederses each word
#  in the string. All spaces in the string should be retained.

# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    to_list = text.split(' ')
    reversed = ''
    for word in to_list:
        reversed += word[::-1] + ' '
    result = reversed.strip()
    return result

# Function driver

print('RESULT::'+reverse_words('This is an example!')+'::STOP')

