# Write a function that takes in a string of one or more words, and returns the
#  same string, but with all five or more letter words reversed(Just like the 
# name of this Kata). Strings passed in will consist of only letters and 
# spaces. Spaces will be included only when more than one word is present.

# Examples: 
# spinWords("Hey fellow warriors") = > returns "Hey wollef sroirraw" 
# spinWords("This is a test") = > returns "This is a test" 
# spinWords("This is another test") = > returns "This is rehtona test"


# My solution

def spin_words(sentence):
    lst = sentence.split()
    res = ''
    for w in lst:
        if len(w) < 5:
            res += w + ' '
        else:
            res += w[::-1] + ' '
    return res.strip()


# Function driver

print(':::'+spin_words('This is a sentence')+':::')
# print(tostring(['T', 'h', 'i', 's', ' ', 'i', 's', ' ',
#               'a', ' ', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e']))
