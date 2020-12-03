import requests
import json
import project_cfg

def readServerData():
    NEW_URL = project_cfg.ThingSpeakCfg.read_url + project_cfg.ThingSpeakCfg.read_key + project_cfg.ThingSpeakCfg.read_header

    get_data= requests.get(NEW_URL).json()
    channel_id = get_data['channel']['id']
        
    field_1 = get_data['feeds']
    print(field_1)  
            
    return (json.loads(field_1[0]["field1"]))