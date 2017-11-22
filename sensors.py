import RPi.GPIO as gpio
import time


def distance():
    gpio.setmode(gpio.BOARD)
    TRIG = 12
    ECHO = 16

    gpio.setwarnings(0)
    gpio.setup(TRIG, gpio.OUT)
    gpio.output(TRIG, 0)
 
    gpio.setup(ECHO, gpio.IN)

    time.sleep(0.1)

    #print "Starting Measurement..."

    gpio.output(TRIG,1)
    time.sleep(0.00001)
    gpio.output(TRIG,0)
    try:
        while gpio.input(ECHO)==0:
            pass
        start = time.time()

        while gpio.input(ECHO) == 1:
            pass
        stop = time.time()

        gpio.cleanup()
    except KeyboardInterrupt:
        gpio.cleanup()

    return  (stop - start) * 17000

def back_distance():
    gpio.setmode(gpio.BOARD)
    TRIG = 12
    ECHO = 18

    gpio.setwarnings(0)
    gpio.setup(TRIG, gpio.OUT)
    gpio.output(TRIG, 0)
 
    gpio.setup(ECHO, gpio.IN)

    time.sleep(0.1)

    #print "Starting Measurement..."

    gpio.output(TRIG,1)
    time.sleep(0.00001)
    gpio.output(TRIG,0)
    try:
        while gpio.input(ECHO)==0:
            pass
        start = time.time()

        while gpio.input(ECHO) == 1:
            pass
        stop = time.time()

        gpio.cleanup()
    except KeyboardInterrupt:
        gpio.cleanup()

    return  (stop - start) * 17000
