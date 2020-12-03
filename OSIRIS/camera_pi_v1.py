import base64
import json
import urllib.request
from time import sleep

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from PIL import Image

THINGSPEAK_WRITEKEY = 'JXB39Y73FYFB1Y4K'


def thingspeak_post(string):
    try:
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
    except:
        print('error: failed to post to thingspeak')
    # print(data)



def auth():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)


def drive(drive):
    try:
        file1 = drive.CreateFile({'title': 'OSIRIS.jpg'})
        img = Image.open('image.jpg')
        # 2. Compressing the image
        img.save("compressed_image.jpg",
                 optimize=True,
                 quality=30)
        file1.SetContentFile("compressed_image.jpg")

        file1.Upload()
        permission = file1.InsertPermission({
            'type': 'anyone',
            'value': 'anyone',
            'role': 'reader'})

    except:
        print('error: failed upload to google drive')

    thingspeak_post(file1['id'])

        # download(file1['id'])
        # file = drive.CreateFile({'id': file1['id']})
        # file.GetContentFile('world.png')

# def download(id):
#     data = urllib.request.urlretrieve('https://docs.google.com/uc?export=download&id=' + id, "00000001.jpg")
#     print(data)

if __name__ == "__main__":
    _auth = auth()
    # while True:
    try:
        drive(_auth)
        print('successful upload')
    except:
        print('error: failed upload')
    sleep(120)

