# Python3
# Test script for rev_words.py

from rev_words import reverse_words

def test_string_0():
    assert(reverse_words('This is an example!') == 'sihT si na !elpmaxe')

def test_string_1():
    assert(reverse_words('double  spaces') == 'elbuod  secaps')

def test_string_2():
    assert(reverse_words('The quick brown fox jumps over the lazy dog.')
           == 'ehT kciuq nworb xof spmuj revo eht yzal .god')

def test_string_3():
    assert(reverse_words('apple') == 'elppa')

def test_string_4():
    assert(reverse_words('a b c d') == 'a b c d')

def test_string_5():
    assert(reverse_words('double  spaced  words') == 'elbuod  decaps  sdrow')

def test_string_6():
    assert(reverse_words('Mihnea Tripsa') == 'aenhiM aspirT')

def test_string_7():
    assert(reverse_words('This is a string.') == 'sihT si a .gnirts')
