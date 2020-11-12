import sqlite3
from time import sleep
import json
from PIL import Image

import requests

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def getPicture(id):
    # print(id)
    file = _auth.CreateFile({'id': id})
    file.GetContentFile('_pic.png')
    im = Image.open(r'_pic.png')
    im.show()


def read():
    URL = 'https://api.thingspeak.com/channels/1161282/feeds.json?api_key='
    KEY = 'F2Q2UUQ0HDTLMK25'
    HEADER = '&results=1'
    NEW_URL = URL + KEY + HEADER
    try:
        data = requests.get(NEW_URL).json()
        # print(data)
        id = data['channel']['id']
        field = data['feeds']
        # print(field)
        # print(field[0]["field1"], field[0]["field2"])
        if 'null' not in field[0]["field1"]:
            print('dataEntry')
            toDatabase(field[0])
        if 'null' not in field[0]["field2"]:
            print('pic')
            getPicture(field[0]["field2"])
        print('success')
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
    # for row in cursor:
    #     print(row['date'], row['alertedSensor'], row['sound'], row['humidity'], row['pressure'], row['temperature'], row['picture'])
    dbconnect.commit()
    dbconnect.close()

def auth():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

if __name__ == "__main__":
    _auth = auth()
    while True:
        read()
        sleep(5)