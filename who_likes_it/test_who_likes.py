from who_likes import likes

def test_basic():
    assert(likes([]) == "no one likes this")

def test_medium():
    assert(likes(["Peter"]) == "Peter likes this")

def test_advanced():
    assert(likes(["Jacob", "Alex"]) == "Jacob and Alex like this")

def test_hard():
    assert(likes(["Max", "John", "Mark"]) == "Max, John and Mark like this")

def test_big_brain_time():
    assert(likes(["Alex", "Jacob", "Mark", "Max"]) == "Alex, Jacob and 2 others like this")
