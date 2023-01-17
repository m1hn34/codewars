# PyTest script for unique_in_order


from unique_ordered import unique_in_order


def test_1():
    assert (unique_in_order('AAAABBBCCDAABBB')
            == ['A', 'B', 'C', 'D', 'A', 'B'])


def test_2():
    assert (unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D'])


def test_3():
    assert (unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3])
