from __future__ import print_function
import pixy
from ctypes import *
from pixy import *
import  pynput
from pynput import keyboard
from pynput.keyboard import Listener
import subprocess
import os
import time
#from picamera import PiCamera

# Constants #
PID_MAXIMUM_INTEGRAL      =  2000
PID_MINIMUM_INTEGRAL      = -2000
ZUMO_BASE_DEADBAND        =    20
PIXY_RCS_MAXIMUM_POSITION =  1000
PIXY_RCS_MINIMUM_POSITION =     0
PIXY_RCS_CENTER_POSITION  = ((PIXY_RCS_MAXIMUM_POSITION - PIXY_RCS_MINIMUM_POSITION) / 2)
MINIMUM_BLOCK_AGE_TO_LOCK =    30
PAN_GAIN                  =   400
TILT_GAIN                 =   500     


pan = 500
tilt = 500
pixy.init ()
pixy.set_servos(pan,tilt)

def takeStill():
    time.sleep(0.5)
    print("\nTaking still please wait...")
    try:    
        cmd = "raspistill -vf -o image.jpg"
        subprocess.call(cmd, shell=True)
        print("Still saved!\n")
    except:
        print("raspistill failed")
        
    time.sleep(0.5)
    print("\nUploading to Google Drive...")
    try:
        cmd = "python camera_pi_v1.py"
        subprocess.call(cmd,shell = True)
        print("Upload success")
    except:
        print("Upload failed")
    
    
def moveRight():
    global pan
    pan = pan+100
    pixy.set_servos(pan,tilt)
    print('\nright success')
    
    
def moveLeft():
    global pan
    pan = pan-100
    pixy.set_servos(pan,tilt)
    print('\nleft success')

def moveUp():
    global tilt
    tilt = tilt-100
    pixy.set_servos(pan,tilt)
    print('\nup success')
    
def moveDown():
    global tilt
    tilt = tilt+100
    pixy.set_servos(pan,tilt)
    print('\ndown success')
    

def on_press(key):
    key2 = str(format(key))
    #print(str(format(key))," ",format(key)," ",key2)    
    if (key2.strip("'")=='d'):      
        moveRight()
    elif (key2.strip("'")=='a'):
        moveLeft()
    elif (key2.strip("'")=='w'):
        moveUp()
    elif (key2.strip("'")=='s'):
        moveDown()
    elif (key2.strip("'")=='e'):
        takeStill()
    else:
        print("\nNot a valid input")
        
        

def runTest():
    print("Running Test...")
    try:
        moveRight()
        time.sleep(0.5)
        moveLeft()
        time.sleep(0.5)
        moveUp()
        time.sleep(0.5)
        moveDown()
        #takeSnap()
        print("Test Successful")
    except:
        print("Error: Testing servos failed")


def on_release(key):
    global tilt
    global pan
    #print("Tilt:",tilt,"Pan:",pan)

#runTest()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()








            
        

 

