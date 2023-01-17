# PyTest for consec.py

from multiprocessing.context import assert_spawning
from consec import longest_consec


def test_0():
    assert(longest_consec(["zone", "abigail", "theta",
           "form", "libe", "zas"], 2) == 'abigailtheta')


def test_1():
    assert(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx",
           "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1) == 'oocccffuucccjjjkkkjyyyeehh')


def test_2():
    assert(longest_consec([], 3) == '')


def test_3():
    assert(longest_consec(
        ["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2) == 'wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck')


def test_4():
    assert(longest_consec(
        ["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2) == 'wlwsasphmxxowiaxujylentrklctozmymu')


def test_5():
    assert(longest_consec(
        ["zone", "abigail", "theta", "form", "libe", "zas"], -2) == '')


def test_6():
    assert(longest_consec(["it", "wkppv", "ixoyx", "3452",
           "zzzzzzzzzzzz"], 3) == 'ixoyx3452zzzzzzzzzzzz')


def test_7():
    assert(longest_consec(
        ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15) == '')


def test_8():
    assert(longest_consec(
        ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0) == '')
