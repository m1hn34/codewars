# PyTest for alternating_split

from alternating_split import decrypt, encrypt

# encryption test


def test_0():
    assert(encrypt("This is a test!", 0) == "This is a test!")


def test_2():
    assert(encrypt("This is a test!", 1) == "hsi  etTi sats!")


def test_4():
    assert(encrypt("This is a test!", 2) == "s eT ashi tist!")


def test_6():
    assert(encrypt("This is a test!", 3) == " Tah itse sits!")


def test_8():
    assert(encrypt("This is a test!", 4) == "This is a test!")


def test_10():
    assert(encrypt("This is a test!", -1) == "This is a test!")


def test_12():
    assert(encrypt("This kata is very interesting!", 1)
           == "hskt svr neetn!Ti aai eyitrsig")


def test_14():
    assert(encrypt("", 0) == "")


def test_16():
    assert(encrypt(None, 0) == None)


# decryption test
def test_1():
    assert(decrypt("This is a test!", 0) == "This is a test!")


def test_3():
    assert(decrypt(" Tah itse sits!", 3) == "This is a test!")


def test_5():
    assert(decrypt("s eT ashi tist!", 2) == "This is a test!")


def test_7():
    assert(decrypt(" Tah itse sits!", 3) == "This is a test!")


def test_9():
    assert(decrypt("This is a test!", 4) == "This is a test!")


def test_11():
    assert(decrypt("This is a test!", -1) == "This is a test!")


def test_13():
    assert(decrypt("hskt svr neetn!Ti aai eyitrsig", 1)
           == "This kata is very interesting!")


def test_15():
    assert(decrypt("", 0) == "")


def test_16():
    assert(decrypt(None, 0) == None)
