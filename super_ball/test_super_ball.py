# PyTest script for super_ball.py
# this is obviously wrong... :(

# TODO learn how to unit test classe with PyTest


import super_ball
from super_ball import Ball


def test_1(self):
    ball = Ball()
    assert ball.ball_type() == 'regular'


def test_2(self):
    ball2 = Ball('super')
    assert ball2.ball_type('super') == 'super'
