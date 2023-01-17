'''
Write a function that takes an integer as input, and returns the number of bits
that are equal to one in the binary representation of that number. You can
guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function
should return 5 in this case
'''
# def countBits(n):
#     b = format(n, 'b')
#     cb = 0
#     for i in b:
#         if i == '1':
#             cb += 1
#     return cb

# Simpler
def countBits(n):
    return bin(n).count('1')

def countStrBits(st):
    return ' '.join(format(ord(x), 'b') for x in st)


# Function driver
print(countStrBits('mihnea'))