# PyTest script for string_incrementer.py


from string_incrementer import increment_string


def test_1():
    assert (increment_string("foo") == "foo1")


def test_2():
    assert (increment_string("foobar001") == "foobar002")


def test_3():
    assert (increment_string("foobar1") == "foobar2")


def test_4():
    assert (increment_string("foobar00") == "foobar01")


def test_5():
    assert (increment_string("foobar99") == "foobar100")


def test_6():
    assert (increment_string("foobar099") == "foobar100")


def test_7():
    assert (increment_string("fo99obar99") == "fo99obar100")


def test_8():
    assert (increment_string("") == "1")
