import requests
import json
import nexmo


URL = 'https://api.thingspeak.com/channels/1161282/fields/1.json?api_key='
KEY = 'F2Q2UUQ0HDTLMK25'
HEADER = '&results=1'
NEW_URL = URL+KEY+HEADER
print(NEW_URL)
    
get_data= requests.get(NEW_URL).json()
channel_id = get_data['channel']['id']
     
field_1 = get_data['feeds']   
print(field_1[0])
        
data = json.loads(field_1[0]["field1"])
humidity = data['humid']
pressure = data['press']
temp = data['temp']
pitch = data['pitch']
roll = data['roll']
yaw = data['yaw']

client = nexmo.Client(key='a7d39d67', secret='42JRTUoahA6MkY9k')

if (humidity > 35):
    if (temp < 50):       
        if (pressure < 950 or pressure > 1100):
            client.send_message({
            'from': '12504835024',
            'to': '16479936650',
            'text': 'The humidity, temperature and pressure is abnormal!',
            })
        else:
            client.send_message({
            'from': '12504835024',
            'to': '16479936650',
            'text': 'The humidity and temperature is abnormal!',
            })
    
    else:
        if (pressure < 950 or pressure > 1100):
            client.send_message({
            'from': '12504835024',
            'to': '16479936650',
            'text': 'The humidity and pressure is abnormal!',
            })      
        else:
            client.send_message({
            'from': '12504835024',
            'to': '16479936650',
            'text': 'The humidity is abnormal!',
            })
            
else:
    if (temp < 50):       
        if (pressure < 950 or pressure > 1100):
            client.send_message({
            'from': '12504835024',
            'to': '16479936650',
            'text': 'The temperature and pressure is abnormal!',
            })
        else:
            client.send_message({
            'from': '12504835024',
            'to': '16479936650',
            'text': 'The temperature is abnormal!',
            })
    
    else:
        if (pressure < 950 or pressure > 1100):
            client.send_message({
            'from': '12504835024',
            'to': '16479936650',
            'text': 'The pressure is abnormal!',
            })      
              
