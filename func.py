import RPi.GPIO as gpio
import time

def init():

        gpio.setmode(gpio.BOARD)
        gpio.setup(7, gpio.OUT)
        gpio.setup(11, gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(15, gpio.OUT)

def forward(tf):


    print 'Moving Forward...'
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(7, False)  #New Line
    gpio.output(15, False) #New Line

    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):

    print 'Moving Backward...'
    gpio.output(7, True)
    gpio.output(15, True)
    gpio.output(11, False) #New Line
    gpio.output(13, False) #New Line

    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):


    print 'Turning Left...'
    gpio.output(11, False)
    gpio.output(7, False)  #New Line
    gpio.output(13, True) #New Line
    gpio.output(15, False) #New Line
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):


    print 'Turning Right...'
    gpio.output(13, False)
    gpio.output(7, False)  #New Line
    gpio.output(11, True) #New Line
    gpio.output(15, False) #New Line

    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):



    print 'Pivoting Left...'
    gpio.output(11, False)
    gpio.output(15, False)
    gpio.output(7, True) #New Line
    gpio.output(13, True) #New Line
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):



    print 'Pivoting Right...'
    gpio.output(7, False)
    gpio.output(13, False)
    gpio.output(11, True) #New Line
    gpio.output(15, True) #New Line
    time.sleep(tf)
    gpio.cleanup()
