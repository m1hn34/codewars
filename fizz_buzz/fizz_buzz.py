'''
Return an array containing the numbers from 1 to N, where N is 
the parametered value. N will never be less than 1.

Replace certain values however if any of the following conditions are met:

If the value is a multiple of 3: use the value 'Fizz' instead
If the value is a multiple of 5: use the value 'Buzz' instead
If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead

fizzbuzz(10) => [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz']
'''


# def fizzbuzz(n):
#     genList = list(range(1, n + 1))
#     outList = ['Fizz' if (i % 3 == 0) else 'Buzz' if (i % 5 == 0) else 'FizzBuzz' if (i % 3) and (i % 5) == 0 else i for i in genList]
#     return outList


def fizzbuzz(n):
    genList = list(range(1, n + 1))
    outList = ['FizzBuzz' if (i % 3 == 0) and (i % 5 == 0) else 'Fizz' if (i % 3 == 0) else 'Buzz' if (
        i % 5 == 0) else i for i in genList]
    return outList


# function driver
print(fizzbuzz(30))
