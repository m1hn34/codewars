'''
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher 
this! kata. Here are the conditions:

Your message is a string containing space separated words.

You need to encrypt each word in the message using the following rules:
- The first letter must be converted to its ASCII code.
- The second letter must be switched with the last letter
Keepin' it simple: There are no special characters in the input.

Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
'''


# 1st Method
def encrypt_this(text):
    text = text.split(' ')
    encrypted = []
    for word in text:
        if len(word) < 3:
            encrypted.append(
                str(ord(word[0])) + word[1])
            encrypted.append(" ")
        else:
            encrypted.append(
                str(ord(word[0])) + word[-1] + word[2:-1:] + word[1]
            )
            encrypted.append(" ")
    text = "".join(encrypted)
    return text.strip()


# debug
a = "A wise old owl lived in an oak"
b = "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
print(encrypt_this(a) == b)
print(encrypt_this(a))
