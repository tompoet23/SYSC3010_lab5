# SYSC 3010 PROJECT - OSIRIS SECURITY SYSTEM
#
# AUTHOR: Timothy Knowles
#
# VERSION: November 24th, 2020
# 
# SENSORY DATA FROM RASPBERRY PI PUSH TO THINGSPEAK SERVER 
#
# CONFIGURATION FROM : "project_cfg.py"
# TEST SUITE FROM : "sensor_pi_pytest.py"


#for unit test framework
import pytest

#for time formatting for values to thingspeak
import time
from datetime import datetime
from time import sleep
from time import asctime
import threading

#all necessary for uploading to thingspeak
import urllib.request
import requests
import http.client
import urllib.parse

#import json module for formatting upload to thingspeak
import json

#import config file
import project_cfg

#if the config file dictates emulator will be used
if (project_cfg.DebugCfg.emulator == True):
    
    #import the emulator module
    import sense_emu

    #instanties emulator object for method calls
    sense = sense_emu.SenseHat()

#if the config file dictates the actual sense hat will be used
if (project_cfg.DebugCfg.hardware == True):

    #import sense hat module
    import sense_hat

    #instantiate sense hat object for method calls
    sense = sense_hat.SenseHat()

#define object to store current sensory values
class currentValues:
    def __init__(self,temperature,humidity,pressure,gyro):
        self.temperature=temperature
        self.humidity = humidity
        self.pressure = pressure
        self.gyro = gyro

#define object to store pitch roll and yaw in single gyroscope object
class gyroValues:
    def __init__(self,pitch,roll,yaw):
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw

#def method to give prompt and time to perform physical hardware test on the sense hat
def hardwareTest(test_name):

    #prompt user for which test and countdown...
    sense.show_message(test_name + " TEST IN:", scroll_speed = (0.08))
    sense.show_message("5")
    sense.show_message("4")
    sense.show_message("3")
    sense.show_message("2")
    sense.show_message("1")

    #show green screen for 5 seconds
    sense.clear(0,255,0)
    sleep(5)

    #clear screen to show time for test has concluded
    sense.clear(0,0,0)


#method for writing data to the thingspeak server
def thingspeak_post(post_temp,post_humid,post_press,post_gyro):

    #string creations for printing to console the values being posted to server
    temp_message = 'Temp = %d Deg C' % (post_temp)
    humidity_message = 'Humidity = %d %%' % (post_humid)
    pressure_message = 'Pressure = %d mBar' % (post_press)
    gyro_pitch = 'Pitch = %d, ' %(post_gyro.pitch)
    gyro_roll = 'Roll = %d, ' %(post_gyro.roll)
    gyro_yaw = 'Yaw = %d ' %(post_gyro.yaw)
    gyro_message = gyro_pitch + gyro_roll + gyro_yaw

    #create object to store the values that were uploaded (for testing purposes)
    uploadedVals = currentValues(post_temp,post_humid,post_press,post_gyro)

    #print to console the created strings
    print(datetime.now())
    print(temp_message)
    print(humidity_message)
    print(pressure_message)
    print(gyro_message)
    print(' ')

    #format data through json
    data = json.dumps({'temp':post_temp,'humid':post_humid,'press':post_press,'pitch':post_gyro.pitch,'roll':post_gyro.roll,'yaw':post_gyro.yaw},separators=(',',':'))
    HEADER='&field1={}'.format(data)

    #create appropriate string for url for posting to thingspeak
    NEW_URL = project_cfg.ThingSpeakCfg.write_url + project_cfg.ThingSpeakCfg.write_key + HEADER

    #post to the thingspeak server via created url
    data=urllib.request.urlopen(NEW_URL)

    #return the values that were uploaded (testing purposes)
    return uploadedVals

#method to pull sense hat temperature sensor value (facilitates testing)
def getTemp():
    return round(sense.get_temperature())

#method to pull sense hat humidity sensor value (facilitates testing)
def getHumid():
    return round(sense.get_humidity())

#method to pull sense hat pressure sensor value (facilitates testing)
def getPressure():
    return round(sense.get_pressure())

#method to pull sense hat temperature from humidity sensor value (facilitates testing)
def getTempFromHumid():
    return round(sense.get_temperature_from_humidity())

#method to pull gyroscope orientation sensor values (facilitates testing)
def getGyro():
    gyroData = sense.get_gyroscope()
    rawPitch = round(gyroData["pitch"],1)
    rawRoll = round(gyroData["roll"],1)
    rawYaw = round(gyroData["yaw"],1)
    return gyroValues(rawPitch,rawRoll,rawYaw)

#method to return a ping for all current sensory values
def currentValQuery():
    return (currentValues(getTemp(),getHumid(),getPressure(),getGyro()))


if __name__ == "__main__":
    
    #continously write to the thingspeak server the sensory values
    while True:

        #ping current sensor values
        curr = currentValQuery()
        uploaded = thingspeak_post(curr.temperature,curr.humidity,curr.pressure,curr.gyro)

        #wait 5 seconds before pinging again
        sleep(5)