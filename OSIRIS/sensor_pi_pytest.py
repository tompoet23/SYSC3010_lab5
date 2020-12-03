# SYSC 3010 PROJECT - OSIRIS SECURITY SYSTEM
#
# AUTHOR: Timothy Knowles
#
# VERSION: November 24th, 2020
# 
# TESTING SUITE FOR SENSOR PI SCRIPT ("sensor_pi_v4.py")
#
# CONFIGURATION FROM : "project_cfg.py"


#import testing framework
import pytest

#import scrip being tested
from sensor_pi_v4 import *

#import config file for test values, etc...
import project_cfg

#set test values as per config file
predefinedTemp = project_cfg.TestingCfg.test_temp
predefinedPressure = project_cfg.TestingCfg.test_press
predefinedHumidity = project_cfg.TestingCfg.test_humid
predefinedPitch = project_cfg.TestingCfg.test_pitch
predefinedRoll = project_cfg.TestingCfg.test_roll
predefinedYaw = project_cfg.TestingCfg.test_yaw 

#setup gyro object to store pitch, roll ,yaw
gyroPredefined = gyroValues(predefinedPitch,predefinedRoll,predefinedYaw)

''' ~~~~~~~~~~~~ SOFTWARE TEST ~~~~~~~~~~~~ '''

#if config warrants emulator for software test..
if (project_cfg.DebugCfg.emulator == True):

    #import the sense hat module
    import sense_emu

    #instantiante sense hat object for method calls
    sense = sense_emu.SenseHat()

    #define test to ensure temp values are pulled correctly (test values == sensor values)
    def test_getTemp():

        assert(getTemp() == predefinedTemp)
        assert(getTemp() != 0)
    
    #define test to ensure humid values are pulled correctly (test values == sensor values)
    def test_getHumid():

        assert(getHumid() == predefinedHumidity)
        assert(getHumid() != 0)
    
    #define test to ensure pressure values are pulled correctly (test values == sensor values)
    def test_getPressure():

        assert(getPressure() == predefinedPressure)
        assert(getPressure() != 0)

    #define test to ensure gyroscope values are pulled correctly (test values == sensor values)
    def test_getGyro():
        assert(getGyro().pitch == gyroPredefined.pitch)
        assert(getGyro().roll == gyroPredefined.roll)
        assert(getGyro().yaw == gyroPredefined.yaw)

    #define test to ensure all current values query is correct (test values == sensor values)
    def test_CurrValQuery():

        #create object of test values
        testValues = currentValues(predefinedTemp,predefinedHumidity,predefinedPressure,gyroPredefined)

        #create object of sensor values
        valQuery = currentValQuery()

        #ensure the values are identical
        assert(valQuery.temperature == testValues.temperature)
        assert(valQuery.humidity == testValues.humidity)
        assert(valQuery.pressure == testValues.pressure)
        assert(valQuery.gyro.pitch == testValues.gyro.pitch)
        assert(valQuery.gyro.roll == testValues.gyro.roll)
        assert(valQuery.gyro.yaw == testValues.gyro.yaw)

    #test for ensuring the values being uploaded to thingspeak server are correct
    def test_thingspeak_post():
        
        #upload values to thingspeak using test values
        uploadedVals = thingspeak_post(predefinedTemp,predefinedHumidity,predefinedPressure,gyroPredefined)

        #ensure the returned objects properties are equal to the test values
        assert(uploadedVals.temperature == predefinedTemp)
        assert(uploadedVals.humidity == predefinedHumidity)
        assert(uploadedVals.pressure == predefinedPressure)


''' ~~~~~~~~~~~~ HARDWARE TEST ~~~~~~~~~~~~ '''

#if config dictates that sense hat hardware is to be tested...
if (project_cfg.DebugCfg.hardware == True):
    #import sense hat module
    import sense_hat

    #instantiated sense hat object for method calls
    senseHW = sense_hat.SenseHat()

    #test to make sure temperature values are within feasible range
    def test_getTemp():
        assert(senseHW.get_temperature() >> -100)
        assert(senseHW.get_temperature() << 400)

    #test to make sure the humidity values are within feasible range 
    def test_getHumid():
        assert(senseHW.get_humidity() >> -1)
        assert(senseHW.get_humidity() << 101)
    
    #test to make sure the pressure values are within feasible range
    def test_getPressure():
        assert(senseHW.get_pressure() >> 200)
        assert(senseHW.get_pressure() << 1300)
    
    #test to make sure the temperature reading from temperature sensor is identical to temperature reading from the humidity sensor
    def test_tempVsHumidTemp():
        assert(senseHW.get_temperature_from_humidity() == senseHW.get_temperature())

    #test to make sure change in environment that warrants temp value change manifests
    def test_tempChange():
        #take current sensory values
        beforeVals = currentValQuery()

        #begin the process of physically  changing of environment for different temperature (gives enough time)
        hardwareTest("TEMPERATURE CHANGE")

        #query current sensory vals after 
        afterVals = currentValQuery()

        #the value should be different since temperature was changed
        assert(beforeVals.temperature != afterVals.temperature)

    #test to make sure the change in orientation warrants gyroscope values that reflect that
    def test_gyroChange():
        #take current sensory values
        beforeVals = currentValQuery()

        #begin the physical changing of environment for different orientation (gives enough time)
        hardwareTest("ORIENTATION CHANGE")

        #query current sensory vals after 
        afterVals = currentValQuery()

        #the orientation values should be different since it was physically changed
        assert(beforeVals.gyro.pitch != afterVals.gyro.pitch)
        assert(beforeVals.gyro.roll != afterVals.gyro.roll)
        assert(beforeVals.gyro.yaw != afterVals.gyro.yaw)