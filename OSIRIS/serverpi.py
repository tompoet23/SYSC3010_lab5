import requests
import json
import unittest

class read(unittest.TestCase):
    def read_data_thingspeak():
        URL = 'https://api.thingspeak.com/channels/1161282/fields/1.json?api_key='
        KEY = 'F2Q2UUQ0HDTLMK25'
        HEADER = '&results=1'
        NEW_URL = URL+KEY+HEADER
        print(NEW_URL)
    
        get_data= requests.get(NEW_URL).json()
        channel_id = get_data['channel']['id']
    
        temperature = get_data['feeds']['temperature']
        humidity = get_data['feeds']['humidty']
        pressure = get_data['feeds']['pressure']
        
        self.assertTrue(temperature < 50, msg="There is a possibility of a fire")
        self.assertTrue(humidity < 35, msg="The air is dry, with a possibility of a fire")
        self.assertTrue(pressure < 90 || pressure > 120, msg="The pressure is not in normal ranges. There could be a leaky roof or air is entering the room. ")
    
        
        
if __name__ == '__main__':
    read_data_thingspeak()
