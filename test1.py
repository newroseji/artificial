#! /usr/bin/python
from sensors import distance
from func import init
from func import pivot_left, pivot_right
import random


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


def forward(tf):
    print 'Moving Forward...'
    gpio.output(7, True)
    gpio.output(13, True)
    gpio.output(11, False)  # New Line
    gpio.output(15, False)  # New Line

    dist = distance()
    if dist <= 15:
        test_autonomy()


    time.sleep(tf)
    gpio.cleanup()


def test_autonomy():
    tf = 0.030
    init()
    forward(tf)
    check_process()


test_autonomy()
