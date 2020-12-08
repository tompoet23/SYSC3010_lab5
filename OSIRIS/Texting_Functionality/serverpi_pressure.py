# SYSC 3010 PROJECT - OSIRIS SECURITY SYSTEM
#
# AUTHOR: Timothy Knowles & Monishkumar Sivakumar
#
# VERSION: December 3rd, 2020
# 
# Continuously poll ThingSpeak server for pressure values and if they become abnormal,
# send a text to given phone.
#


#necessary modules for ThingSpeak data pulling
import requests
import json
import readDataFunction

#necessary module to send text message
import nexmo

#project config file for correct values: read_key, etc...
import project_cfg

from time import sleep

def pollPressure():

    #store ThingSpeak server data
    data = readDataFunction.readServerData()

    #assign variables to the various parsed data values
    humidity = data['humid']
    pressure = data['press']
    temperature = data['temp']
    pitch = data['pitch']
    roll = data['roll']
    yaw = data['yaw']

    #instantiate client for text message receiver
    client = nexmo.Client(key='a7d39d67', secret='42JRTUoahA6MkY9k')

    #keep polling ThingSpeak values while they are within acceptable range
    while (pressure > 400):
    
        data = readDataFunction.readServerData()
        pressure = data['pressure']
        sleep(5)
    
    #if the pressure value is every outside of acceptable range, send text message
    client.send_message({
                'from': '12504835024',
                'to': '16479936650',
                'text': 'The pressure is abnormal!',
                })