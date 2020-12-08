# SYSC 3010 PROJECT - OSIRIS SECURITY SYSTEM
#
# AUTHOR: Timothy Knowles & Monishkumar Sivakumar
#
# VERSION: December 3rd, 2020
# 
# Continuously poll ThingSpeak server for temperature/humidity and pressure values and if they become abnormal,
# send a text to given phone. Main file
#

#import each script responsible for humiditiy,temperature and pressure
import serverpi_humidity
import serverpi_temperature
import serverpi_pressure

#main function
if __name__ == "__main__":
    
    #begin pollings
    serverpi_humidity.pollHumidity()
    serverpi_temperature.pollTemperature()
    serverpi_pressure.pollPressure()