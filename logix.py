import RPi.GPIO as gpio
import time
import sys
from sensors import distance
from func import init,forward,reverse,turn_left,turn_right
from func import pivot_left,pivot_right
import random
def check_front():

    tf = 0.030

    init()
    dist = distance()
    print 'The distance is now : ', dist
    if dist <15:
        print ('Too close,', dist)
        init()
        reverse(2)

        dist = distance()
        if dist<15:
            print('Too close,',dist)
            init()
            pivot_left(3)
            init()
            reverse(2)
            dist = distance()
            if dist <15:
                print('Too close, giving up', dist)
                sys.exit()

    if dist>15:
        print 'The distance is now : ', dist
        init()
        forward(tf)

def autonomy():
    tf = 0.030

    for n in range(10):
        check_front()
        init()
        forward(tf)

    x = random.randrange(0, 4)
    print('Random value of X is', x)

    if x == 0:
        for y in range(30):
            check_front()
            init()
            forward(tf)
    elif x == 1:
        for y in range(30):
            check_front()
            init()
            forward(tf)
    elif x == 2:
        for y in range(30):
            check_front()
            init()
            pivot_right(tf)
    elif x == 3:
        for y in range(30):
            check_front()
            init()
            pivot_left(tf)
