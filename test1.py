#! /usr/bin/python
from sensors import distance
from func import init, forward
from func import pivot_left, pivot_right
import random


def test_autonomy():
    forward()
    check_process()


def check_process():
    tf = 0.030

    init()
    dist = distance()
    print 'The distance is now : ', dist

    if dist < 15:
        print ('Too close,', dist)
        init()

        x = random.randrange(0, 2)

        if x == 0:
            pivot_left(tf)
        elif x == 1:
            pivot_right(tf)

    test_autonomy()


test_autonomy()
