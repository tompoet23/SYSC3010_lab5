# SYSC 3010 PROJECT - OSIRIS SECURITY SYSTEM
#
# AUTHOR: Monishkumar Sivakumar
#
# VERSION: December 8th, 2020
# 
# Code that senses motion using motion sensor and then turns on sensehat emulator led
#
         
#import libraries
from sense_emu import SenseHat
import RPi.GPIO as GPIO
import time

#configure the raspberry pi board to look at pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
PIR_PIN = 8 #attachs the pin numberthe motion sensor is attached to, to a variable
GPIO.setup(PIR_PIN,GPIO.IN)

led = GPIO.input(8) #checks for the input coming from the pin the motion sensor is attached to

sense = SenseHat() #initializing the sensehat emulator

#led colors
y = (255, 255, 0)
x = (0, 0, 0)

#led format for when its on
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

#led format for when its off
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

#attachs led format to two different screens
screen1 = on
screen2 = off

#try statement to check if there is an error with the motion sensor
try:
    if led == 1: #if the motion sensor detects motion, the on led screen will be displayed. A certain time is given to check for motion
        sense.set_pixels(screen1)
        print("Motion was detected")
        time.sleep(1)
    else: #if the motion sensor doesn't detect motion, the off led screen will be displayed. A certain time is given to check for motion
        sense.set_pixels(screen2)
        print("No motion was detected")
        time.sleep(1)
except: #what happens if there is something wrong with the motion detector
    print("Something went wrong with the motion detector")
