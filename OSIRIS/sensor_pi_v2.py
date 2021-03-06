#CHANGE TO sense_hat, for testing, removed
#import sense_emu
#CHANGE TO sense_hat

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
#sense = sense_emu.SenseHat()

def thingspeak_post(post_temp,post_humid,post_press):
    print (post_temp, post_humid, post_press)
    #threading.Timer(15,thingspeak_post).start()
    URl='https://api.thingspeak.com/update?api_key='
    KEY= THINGSPEAK_WRITEKEY
    data = json.dumps({'temp': post_temp, 'humid': post_humid, 'press': post_press})
    HEADER='&field1={}'.format(data)
    NEW_URL=URl+KEY+HEADER
    #print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    #print(data)

if __name__ == "__main__":
    test = True
    while True:
        if not test:
            temp = round(sense.get_temperature())
            humidity = round(sense.get_humidity())
            pressure = round(sense.get_pressure())
            orientation = sense.get_orientation()
            compass = sense.get_compass()
            gyro = sense.get_gyroscope()
            accel = sense.get_accelerometer()

            temp_message = 'Temp = %d Deg C' % (temp)
            humidity_message = 'Humidity = %d' % (humidity)
            pressure_message = 'Pressure = %d' % (pressure)
            orientation_message = 'Orient = {}'.format(orientation)
            compass_message = 'North is {}'.format(compass)
            gyro_message = 'Gyro data is {}'.format(gyro)
            accel_message = 'Accel data is {}'.format(accel)

            print(datetime.now())
            print(temp_message)
            print(humidity_message)
            print(pressure_message)
            print(orientation_message)
            print(compass_message)
            print(gyro_message)
            print(accel_message)
            print("\n")
        else:
            temp = random.randint(14, 24)
            humidity = random.randint(50, 90)
            pressure = random.randint(0, 10)

        thingspeak_post(temp, humidity, pressure)

        sleep(5)
