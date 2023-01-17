'''
You need to return a string that looks like a diamond shape when printed on 
the screen, using asterisk (*) characters. Trailing spaces should be removed, 
and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is 
not possible to print a diamond of even or negative size.

Examples

A size 3 diamond:

 *
***
 *
...which would appear as a string of " *\n***\n *\n"

A size 5 diamond:

  *
 ***
*****
 ***
  *
...that is:

"  *\n ***\n*****\n ***\n  *\n"

'''


def diamond(n):
    if (n < 0) or ((n % 2) == 0):
        return None
    else:
        diamond = ''
        for i in range(n):
            diamond += (" " * (n - i) + "*" * (2*i + 1))+"\n"
        for i in range(n-2, -1, -1):
            diamond += (" " * (n - i) + "*" * (2*i + 1))+"\n"
        # TODO remove the trailing "\n" from diamond
        # diamond = diamond.strip()

        return diamond


# debug
print(diamond(3))
if diamond(5) == "  *\n ***\n*****\n ***\n  *\n":
    print(True)
else:
    print(False)
