# Pytest script for time.py

from time_ import format_duration


def test_0():
    assert(format_duration(1) == '1 second')
    assert(format_duration(62) == '1 minute and 2 seconds')
    assert(format_duration(120) == '2 minutes')
    assert(format_duration(3600) == '1 hour')
    assert(format_duration(3662) == '1 hour, 1 minute and 2 seconds')
