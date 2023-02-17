# PyTest script for encrypt.py

from encrypt import encrypt_this


def test_1():
    a = ""
    b = ""
    assert (encrypt_this(a) == b)


def test_2():
    a = "A wise old owl lived in an oak"
    b = "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
    assert (encrypt_this(a) == b)


def test_3():
    a = "The more he saw the less he spoke"
    b = "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"
    assert (encrypt_this(a) == b)


def test_4():
    a = "The less he spoke the more he heard"
    b = "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"
    assert (encrypt_this(a) == b)


def test_5():
    a = "Why can we not all be like that wise old bird"
    b = "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"
    assert (encrypt_this(a) == b)


def test_6():
    a = "Thank you Piotr for all your help"
    b = "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"
    assert (encrypt_this(a) == b)
