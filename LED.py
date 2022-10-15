#!/usr/bin/env python
import RPi.GPIO as GPIO #RPi.GPIO can be referred as GPIO from now
import time

ledPin = 22   #pin22

def setup():
    GPIO.setmode(GPIO.BOARD)     #GPIO Numbering of pins
    GPUO.setup(ledPin,GPIO.OUT)  #set ledPin as output
    GPIO.output(ledPin, GPIO.LOW) #set ledpin to LOW to turn off the LED

def loop():
    while True:
        print ('LED on')
        GPIO.out(ledPin,GPIO.HIGH)     #LED on
        time.sleep(1.0)                #wait 1 sec
        print ('LED off')
        GPIO.output(ledpin,GPIO.LOW)    #LED off
        time.sleep(1.0)                 #wait 1 sec
def endprogram():

    GPIO.output(ledPin,GPIO.LOW)       #LED off
    GPIO.cleanup()                     #Release resources

if _name_=='_main_':            #program starts from here
    setup()
    try:
           loop()
    except KeyboardInterupt:   #when 'Ctrl+C' is pressed,the destroy() will be executed.
           endprogram()
