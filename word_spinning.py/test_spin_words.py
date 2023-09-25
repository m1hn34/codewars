# Python3
# Pytest script for spin_words.py

from spin_words import spin_words


def test_0():
    assert (spin_words('Welcome') == 'emocleW')
    assert (spin_words('Hey fellow warriors') == 'Hey wollef sroirraw')
    assert (spin_words('This is a test') == 'This is a test')
    assert (spin_words('This is another test') == 'This is rehtona test')
