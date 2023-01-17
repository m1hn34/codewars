# Write a function `greet` that returns "hello world!"
def greet():
    message = 'Sure, this is about as easy as it gets. But how clever can you be to create the most creative hello world you can think of? What is a "hello world" solution you would want to show your friends?'
    out = message[7] + message[23] + \
        (message[49])*2 + message[60] + message[99:105]
    return out

# function driver
print(greet())
