from printer_errors import printer_error

def test_basic():
    assert(printer_error("aaabbbbhaijjjm") == "0/14")

def test_medium():
    assert(printer_error("aaaxbbbbyyhwawiwjjjwwm") == "8/22")

def test_advanced():
    assert(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz") == "3/56")

