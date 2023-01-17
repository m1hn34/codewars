# PyTest script for two fighters 'fight.py'

from fight import declare_winner


def test_1():
    assert (declare_winner(
        fighter1=("Lew", 10, 2), fighter2=("Harry", 5, 4), first_attacker="Lew") == 'Lew')


def test_2():
    assert (declare_winner(
        fighter1=("Lew", 10, 2), fighter2=("Harry", 5, 4), first_attacker="Harry") == 'Harry')


def test_3():
    assert (declare_winner(
        fighter1=("Harald", 20, 5), fighter2=("Harry", 5, 4), first_attacker="Harry") == 'Harald')


def test_4():
    assert (declare_winner(
        fighter1=("Harald", 20, 5), fighter2=("Harry", 5, 4), first_attacker="Harald") == 'Harald')


def test_5():
    assert (declare_winner(
        fighter1=("Jerry", 30, 3), fighter2=("Harald", 20, 5), first_attacker="Jerry") == 'Harald')


def test_6():
    assert (declare_winner(
        fighter1=("Jerry", 30, 3), fighter2=("Harald", 20, 5), first_attacker="Harald") == 'Harald')
