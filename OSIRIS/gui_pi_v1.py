import io
import sqlite3
from time import sleep
import json
from PIL import Image

import requests
from googleapiclient.http import MediaIoBaseDownload

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# ..\ORISIS\src\assets\pictures / t2.jpeg
IMAGEPATH = r'C:\Users\plipm\WebstormProjects\ORISIS\src\assets\pictures\t.jpeg'


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
        elif 'null' not in field[0]["field2"]:
            print('pic')
            try:
                download_file_from_google_drive(field[0]["field2"])
            except:
                print('error: failed to download')
            try:
                im = Image.open(IMAGEPATH)
                print(im.format)
                if im.format is 'JPEG':
                    im.close()
                    raise
                im.close()
                print('successful image download')
            except:
                print('error: not an image')
            # getPicture(field[0]["field2"])
    except SyntaxError:
        print("connection failed")
        print(SyntaxError)


def toDatabase(entry):
    dbconnect = sqlite3.connect("database")
    dbconnect.row_factory = sqlite3.Row
    cursor = dbconnect.cursor()
    data = json.loads(entry["field1"])
    print(entry)
    print(data)
    cursor.execute("INSERT OR IGNORE INTO sensorTable values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (entry['created_at'],
                    'null',
                    'null',
                    data['humid'],
                    data['press'],
                    data['temp'],
                    'null',
                    data['pitch'],
                    data['yaw'],
                    data['roll']))

    # cursor.execute("SELECT * FROM sensorTable")
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

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)
    if "<html>" in response:
        print('google blocked this request, oops')
        raise
    save_response_content(response)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith(' download_warning'):
            return value

    return None


def save_response_content(response):
    CHUNK_SIZE = 32768

    with open(IMAGEPATH, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


if __name__ == "__main__":
    # _auth = auth()
    while True:
        # getPicture2('17yQeAryg6xeYo_A8YO2TD_Z7Vz7PTamJ')
        # download_file_from_google_drive('17yQeAryg6xeYo_A8YO2TD_Z7Vz7PTamJ')
        read()
        sleep(5)
