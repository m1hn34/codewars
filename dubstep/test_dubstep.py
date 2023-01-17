# Python3
# Pytest script for dubstep.py

from dubstep import song_decoder

def test_0():
    
    # WUB should be replaced by 1 space
    assert(song_decoder('AWUBBWUBC') == 'A B C')

    # multiples WUB should be replaced by only 1 space
    assert(song_decoder('AWUBWUBWUBBWUBWUBWUBC') == 'A B C')

    # heading or trailing spaces should be removed
    assert(song_decoder('WUBAWUBBWUBCWUB') == 'A B C')

