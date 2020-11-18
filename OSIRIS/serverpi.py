import requests
import json



def read_data_thingspeak():
    URL = 'https://api.thingspeak.com/channels/1161282/fields/1.json?api_key='
    KEY = 'F2Q2UUQ0HDTLMK25'
    HEADER = '&results=1'
    NEW_URL = URL+KEY+HEADER
    print(NEW_URL)

    data = requests.get(NEW_URL).json()
    id = data['channel']['id']
    field = data['feeds']
    print(field[0])
    data = json.loads(field[0]["field1"])
    humidity = data['humid']
    pressure = data['press']
    temperature = data['temp']

    # get_data= requests.get(NEW_URL)
    # data = json.loads(get_data)
    # channel_id = get_data['channel']['id']

    # temperature = get_data['feeds']['temperature']
    # humidity = get_data['feeds']['humidty']
    # pressure = get_data['feeds']['pressure']

    print(temperature, humidity, pressure)
    # self.assertTrue(temperature < 50, msg="There is a possibility of a fire")
    # self.assertTrue(humidity < 5, msg="The air is dry, with a possibility of a fire")
    # self.assertTrue(pressure < 10, msg="The pressure is high")
    
        
        
if __name__ == '__main__':
    read_data_thingspeak()