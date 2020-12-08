# SYSC 3010 PROJECT - OSIRIS SECURITY SYSTEM
#
# AUTHOR: Timothy Knowles
#
# VERSION: December 3rd, 2020
# 
# central configuration file for Thingspeak, Sql database, and google drivE
#
# CONFIG VALUES FOR: - ("sensor_pi_v4.py")
#                    - ("serverpi_humidity.py")
#                    - ("serverpi_pressure.py") 
#                    - ("serverpi_temperature.py") 
#                    - ("serverpi3.py") 
#                    - ("readDataFunction.py)                  



#thingspeak server configuration properties
class ThingSpeakCfg:
    #thingspeak write key
    write_key = 'JXB39Y73FYFB1Y4K'

    #thingspeak write url
    write_url = 'https://api.thingspeak.com/update?api_key='
    
    #thingspeak read url
    read_url = 'https://api.thingspeak.com/channels/1161282/fields/1.json?api_key='

    #thingspeak read key
    read_key = 'F2Q2UUQ0HDTLMK25'

    #thingspeak read header first portion
    read_header = '&results=1'

#sql database configuration properites
class SqlCfg:
    #database name
    db_name = 'database'

#debuf configuration properties
class DebugCfg:
    #is the actual sense hat being used...
    hardware = False

    #is the emulator being used
    emulator = True

#google drive configuration properties
class GoogleDriveCfg:
    #google drive url
    url = 'https://docs.google.com/uc?export=download'

#test values configuration properites  
class TestingCfg:
    test_temp = 25
    test_press = 1105
    test_humid = 30
    test_pitch = 10
    test_roll = 10
    test_yaw = 10
    
