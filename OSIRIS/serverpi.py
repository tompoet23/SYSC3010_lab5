import requests
import json
import unittest

class read(unittest.TestCase):

    def test_multipleasserts(self):
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

        self.assertTrue(temp < 50, msg="There is a possibility of a fire")

        self.assertTrue(humidity < 35, msg="The air is dry, with a possibility of a fire")

        self.assertTrue(pressure < 950 | pressure > 1100, msg="The pressure is high")
    
        
        
if __name__ == '__main__':
    unittest.main()
