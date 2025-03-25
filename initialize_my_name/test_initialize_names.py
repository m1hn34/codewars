# PyTest script for initialize_names.py

from initialize_names import initialize_names


def test_0():
    name = "Jack Ryan"
    output = "Jack Ryan"
    assert(initialize_names(name) == output)

def test_1():
    name = "Lois Mary Lane"
    output = "Lois M. Lane"
    assert(initialize_names(name) == output)

def test_2():
    name = "Daniel"
    output = "Daniel"
    assert(initialize_names(name) == output)

def test_3():
    name = "Alice Betty Catherine Davis"
    output = "Alice B. C. Davis"
    assert(initialize_names(name) == output)

def test_4():
    name = "John Ronald Reuel Tolkien"
    output = "John R. R. Tolkien"
    assert(initialize_names(name) == output)

def test_5():
    name = "George Raymond Richard Martin"
    output = "George R. R. Martin"
    assert(initialize_names(name) == output)

def test_6():
    name = "Joanne Kathleen Rowling"
    output = "Joanne K. Rowling"
    assert(initialize_names(name) == output)

def test_7():
    name = "J. K. Rowling"
    output = "J. K. Rowling"
    assert(initialize_names(name) == output)

