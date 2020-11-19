#CHANGE To sense_hat, for testing, removed
import pytest
import sense_emu
import time
from datetime import datetime
from time import sleep
from time import asctime
import urllib.request
import requests
import threading
import json
import http.client
import urllib.parse
import json
import random


THINGSPEAK_WRITEKEY = 'JXB39Y73FYFB1Y4K'

#change to sense_hat, for testing, removed
sense = sense_emu.SenseHat()


class currentValues:
    def __init__(self,temperature,humidity,pressure):
        self.temperature=temperature
        self.humidity = humidity
        self.pressure = pressure


def thingspeak_post(post_temp,post_humid,post_press):

    temp_message = 'Temp = %d Deg C' % (post_temp)
    humidity_message = 'Humidity = %d %%' % (post_humid)
    pressure_message = 'Pressure = %d mBar' % (post_press)

    uploadedVals = currentValues(post_temp,post_humid,post_press)

    print(datetime.now())
    print(temp_message)
    print(humidity_message)
    print(pressure_message)
    print(' ')

    URl='https://api.thingspeak.com/update?api_key='
    KEY= THINGSPEAK_WRITEKEY
    data = json.dumps({'temp':post_temp,'humid':post_humid,'press':post_press},separators=(',',':'))
    HEADER='&field1={}'.format(data)
    NEW_URL=URl+KEY+HEADER
    data=urllib.request.urlopen(NEW_URL)

    return uploadedVals

def getTemp():
    return round(sense.get_temperature())

def getHumid():
    return round(sense.get_humidity())

def getPressure():
    return round(sense.get_pressure())

def currentValQuery():
    return (currentValues(getTemp(),getHumid(),getPressure()))

if __name__ == "__main__":

    while True:

        curr = currentValQuery();
        uploaded = thingspeak_post(curr.temperature,curr.humidity,curr.pressure)

        sleep(5)
