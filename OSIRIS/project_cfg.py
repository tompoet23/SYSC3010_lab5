# central configuration file for Thingspeak, Sql database, and google drive

class ThingSpeakCfg:
    write_key = 'JXB39Y73FYFB1Y4K'
    write_url = 'https://api.thingspeak.com/update?api_key='
    
    read_url = 'https://api.thingspeak.com/channels/1161282/feeds.json?api_key='
    read_key = 'F2Q2UUQ0HDTLMK25'
    read_header = '&results=1'
    
class SqlCfg:
    db_name = 'database'
    
class DebugCfg:
    hardware = False
    emulator = True
    
class GoogleDriveCfg:
    url = 'https://docs.google.com/uc?export=download'
    
class TestingCfg:
    test_temp = 25
    test_press = 1105
    test_humid = 30
    test_pitch = 10
    test_roll = 10
    test_yaw = 10
    