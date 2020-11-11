import sqlite3
from time import sleep
import json

import requests


def read():
    URL = 'https://api.thingspeak.com/channels/1161282/fields/1.json?api_key='
    KEY = 'F2Q2UUQ0HDTLMK25'
    HEADER = '&results=1'
    NEW_URL = URL + KEY + HEADER
    try:
        data = requests.get(NEW_URL).json()
        # print(data)
        id = data['channel']['id']
        field = data['feeds']
        print(field)
        toDatabase(field[0])
    except:
        print("connection failed")

def toDatabase(entry):
    dbconnect = sqlite3.connect("database")
    dbconnect.row_factory = sqlite3.Row
    cursor = dbconnect.cursor()
    data = json.loads(entry["field1"])

    cursor.execute("INSERT INTO sensorTable values(?, ?, ?, ?, ?, ?, ?)",
                   (entry['created_at'],
                    'null',
                    'null',
                    data['humid'],
                    data['press'],
                    data['temp'],
                    'null'))

    cursor.execute("SELECT * FROM sensorTable")
    for row in cursor:
        print(row['date'], row['alertedSensor'], row['sound'], row['humidity'], row['pressure'], row['temperature'], row['picture'])
    dbconnect.commit()
    dbconnect.close()

if __name__ == "__main__":
    while True:
        read()
        sleep(5)