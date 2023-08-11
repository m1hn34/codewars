from expand import expanded_form


def test_1():
    assert (expanded_form(12) == "10 + 2")


def test_2():
    assert (expanded_form(42) == "40 + 2")


def test_3():
    assert (expanded_form(70304) == "70000 + 300 + 4")


def test_4():
    assert (expanded_form(123) == "100 + 20 + 3")


def test_5():
    assert (expanded_form(9999999999) ==
            "9000000000 + 900000000 + 90000000 + 9000000 + 900000 + 90000 " +
            "+ 9000 + 900 + 90 + 9")
