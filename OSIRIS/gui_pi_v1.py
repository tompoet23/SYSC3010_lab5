import io
import sqlite3
from time import sleep
import json
from PIL import Image

import requests
from googleapiclient.http import MediaIoBaseDownload

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def getPicture(id):
    # print(id)
    file = _auth.CreateFile({'id': id})
    file.GetContentFile('_pic.png')

    im = Image.open(r'_pic.png')
    im.show()

def getPicture2(id):
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print
        "Download %d%%." % int(status.progress() * 100)

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
            download_file_from_google_drive(field[0]["field2"])
            # getPicture(field[0]["field2"])
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

import requests

def download_file_from_google_drive(id):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response):
    CHUNK_SIZE = 32768

    with open('t2.jpeg', "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

if __name__ == "__main__":
    # _auth = auth()
    while True:
        # getPicture2('17yQeAryg6xeYo_A8YO2TD_Z7Vz7PTamJ')
        # download_file_from_google_drive('17yQeAryg6xeYo_A8YO2TD_Z7Vz7PTamJ')
        read()
        sleep(5)