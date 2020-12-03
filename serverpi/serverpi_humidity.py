import requests
import json
import nexmo
import project_cfg
import readDataFunction
from time import sleep

def pollHumidity():
    data = readDataFunction.readServerData()
    humidity = data['humid']
    pressure = data['press']
    temp = data['temp']
    pitch = data['pitch']
    roll = data['roll']
    yaw = data['yaw']

    client = nexmo.Client(key='a7d39d67', secret='42JRTUoahA6MkY9k')

    while (humidity > 35):
    
        data = readDataFunction.readServerData()
        humidity = data['humid']
        sleep(5)
    
    client.send_message({
                'from': '12504835024',
                'to': '16479936650',
                'text': 'The humidity is abnormal!',
                })

