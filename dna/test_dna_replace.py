# Python3
# Pytest script for dna.py

from dna_replace import DNA_strand

def test_0():
    assert(DNA_strand('AAAA') == 'TTTT')
    assert(DNA_strand('ATTGC') == 'TAACG')
    assert(DNA_strand('GTAT') == 'CATA')
    assert(DNA_strand('AACTGTAT') == 'TTGACATA')
    assert(DNA_strand('CTATGT') == 'GATACA')
