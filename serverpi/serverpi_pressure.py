import requests
import json
import nexmo
import project_cfg
import readDataFunction
from time import sleep

def pollPressure():
    data = readDataFunction.readServerData()
    humidity = data['humid']
    pressure = data['press']
    temperature = data['temp']
    pitch = data['pitch']
    roll = data['roll']
    yaw = data['yaw']

    client = nexmo.Client(key='a7d39d67', secret='42JRTUoahA6MkY9k')

    while (pressure > 400):
    
        data = readDataFunction.readServerData()
        pressure = data['pressure']
        sleep(5)
    
    client.send_message({
                'from': '12504835024',
                'to': '16479936650',
                'text': 'The pressure is abnormal!',
                })