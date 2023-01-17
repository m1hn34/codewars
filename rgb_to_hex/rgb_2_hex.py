
"""
The rgb function is incomplete. Complete it so that passing in RGB decimal
values will result in a hexadecimal representation being returned. Valid
decimal values for RGB are 0 - 255. Any values that fall out of that range must
be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will
not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0, 0, 0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

"""

# my solution = noob**2


def rgb_to_text(a, b, c):
    if a < 0:
        a = 0
    if a > 255:
        a = 255
    if b < 0:
        b = 0
    if b > 255:
        b = 255
    if c < 0:
        c = 0
    if c > 255:
        c = 255

    # set rgb as tuple
    rgb = (a, b, c)

    # return rgb as hex
    return '%02x%02x%02x'.upper() % rgb


# simple solution

def rgb(r, g, b):
    def round(x): return min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


# debug
print(rgb_to_text(-20, 275, 125))
print(rgb(-20, 275, 125))
