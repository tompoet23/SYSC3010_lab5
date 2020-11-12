import base64
import json
import urllib.request
from time import sleep

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

THINGSPEAK_WRITEKEY = 'JXB39Y73FYFB1Y4K'


def thingspeak_post(string):
    print(string)
    # threading.Timer(15,thingspeak_post).start()
    URl = 'https://api.thingspeak.com/update?api_key='
    KEY = THINGSPEAK_WRITEKEY
    # data = json.dumps({'image': string}, separators=(',', ':'))
    # HEADER='&field1={}&field2={}&field3={}'.format(post_temp,post_humid,post_press)
    HEADER = '&field1={},&field2={}'.format('null', string)
    NEW_URL = URl + KEY + HEADER
    print(NEW_URL)
    data = urllib.request.urlopen(NEW_URL)
    # print(data)



def auth():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)


def drive(drive):
    file1 = drive.CreateFile({'title': 'Hello.txt'})
    file1.SetContentFile('t.jpg')
    file1.Upload()
    thingspeak_post(file1['id'])
    # download(file1['id'])
    # file = drive.CreateFile({'id': file1['id']})
    # file.GetContentFile('world.png')

# def download(id):
#     data = urllib.request.urlretrieve('https://docs.google.com/uc?export=download&id=' + id, "00000001.jpg")
#     print(data)

if __name__ == "__main__":
    _auth = auth()
    while True:
        drive(_auth)
        sleep(120)
