from filter_list import filter_list

def test_basic():
    assert(filter_list([1, 2, 'a', 'b']) == [1, 2])

def test_advanced():
    assert(filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15])

def test_supersayan():
    assert(filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123])

