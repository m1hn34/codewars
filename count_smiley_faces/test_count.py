# PyTest script for count.py

from count import count_smileys


def test_1():
    assert (count_smileys([]) == 0)


def test_2():
    assert (count_smileys([':D', ':~)', ';~D', ':)']) == 4)


def test_3():
    assert (count_smileys([':)', ':(', ':D', ':O', ':;']) == 2)


def test_4():
    assert (count_smileys([';]', ':[', ';*', ':$', ';-D']) == 1)
