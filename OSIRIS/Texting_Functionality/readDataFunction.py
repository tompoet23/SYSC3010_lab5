# SYSC 3010 PROJECT - OSIRIS SECURITY SYSTEM
#
# AUTHOR: Timothy Knowles & Monishkumar Sivakumar
#
# VERSION: December 3rd, 2020
# 
# Function definition script to read from ThingSpeak channel
#

#import requests module to read from channel
import requests

#import JSON formatting module
import json

#import project config file for appropriate keys
import project_cfg


def readServerData():
    #create URL string with appropriate keys from config file
    NEW_URL = project_cfg.ThingSpeakCfg.read_url + project_cfg.ThingSpeakCfg.read_key + project_cfg.ThingSpeakCfg.read_header

    #store ThingSpeak server data using json formatting
    get_data= requests.get(NEW_URL).json()

    channel_id = get_data['channel']['id']
    
    #grab field_1 from server data
    field_1 = get_data['feeds']

    #print for debugging purposes
    print(field_1)  
            
    #return the pulled data
    return (json.loads(field_1[0]["field1"]))