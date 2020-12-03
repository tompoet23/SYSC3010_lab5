#import unittest;

#ledSig = 1; #this value is a hardcoded value to test if the motion sensor detects movement

#class light(unittest.TestCase):
#    def test_light(self):
#        self.assertTrue(ledSig == 1, msg="No signal is given to turn LED on") # tests to see if a signal is given to turn led

#if __name__=='__main__':
#   unittest.main()

# import RPi.GPIO as GPIO

#from sensoremu import motion

#gpio = True
#led = motion(gpio)

from sense_emu import SenseHat
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
PIR_PIN = 8
GPIO.setup(PIR_PIN,GPIO.IN)

led = GPIO.input(8)

sense = SenseHat()

y = (255, 255, 0)
x = (0, 0, 0)

on = [
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y,
]

off = [
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
]

screen1 = on
screen2 = off

try:
    if led == 1:
        sense.set_pixels(screen1)
        print("Motion was detected")
        time.sleep(1)
    else:
        sense.set_pixels(screen2)
        print("No motion was detected")
        time.sleep(1)
except:
    print("Something went wrong with the motion detector")