# Python3.9

from __future__ import print_function
from queue import PriorityQueue


def encrypt(text, n):
    odd, eve, result = "", "", ""
    count = 1
    if n < 1:
        return text
    else:
        while count <= n:
            for i, j in enumerate(text):
                if i % 2 == 0:
                    eve += j
                else:
                    odd += j
            result = odd + eve
            eve = ""
            odd = ""
            count += 1
        return result


# driver
# text = "012345"
# n = 5
# encrypted_text = encrypt(text, n)


# TODO
# fix this decription mess

def decrypt(encrypted_text, n):
    odd, eve, result = "", "", ""
    # count = 0
    half = int(len(encrypted_text)/2)
    if n < 1:
        return encrypted_text
    else:

        temp = encrypted_text
    #     while count <= n:

        odd = temp[0:half]
        eve = temp.replace(odd, '')
        temp = eve + odd
    #         count += 1

        return eve


# debugging
print(encrypt("caca in gura ta!", n=1))
print("hsi  etTi sats!")
print()
# print(decrypt("hsi  etTi sats!", n=1))
# print("This is a test!")
