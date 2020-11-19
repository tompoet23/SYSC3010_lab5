import pytest
import sense_emu
from sense_hat import SenseHat
from sensor_pi_v4 import *

sense = sense_emu.SenseHat()
senseHW = SenseHat()

predefinedTemp = 25
predefinedPressure = 1013
predefinedHumidity = 45

#SOFTWARE TEST

def test_getTemp():
    assert(getTemp() == predefinedTemp)
    assert(getTemp() != 0)
    #assert(getTemp() == 100)

def test_getHumid():
    assert(getHumid() == predefinedHumidity)
    assert(getHumid() != 0)
    #assert(getHumid() == 100)

def test_getPressure():
    assert(getPressure() == predefinedPressure)
    assert(getPressure() != 0)
    #assert(getPressure() == 100)

def test_CurrValQuery():
    testValues = currentValues(predefinedTemp,predefinedHumidity,predefinedPressure)
    valQuery = currentValQuery()
    assert(valQuery.temperature == testValues.temperature)
    assert(valQuery.humidity == testValues.humidity)
    assert(valQuery.pressure == testValues.pressure)

def test_thingspeak_post():
    uploadedVals = thingspeak_post(predefinedTemp,predefinedHumidity,predefinedPressure)
    assert(uploadedVals.temperature == predefinedTemp)
    assert(uploadedVals.humidity == predefinedHumidity)
    assert(uploadedVals.pressure == predefinedPressure)

#HARDWARE TEST

def test_getTemp():
    assert(senseHW.get_temperature() > -100)
    assert(senseHW.get_temperature() < 400)

def test_getHumid():
    assert(senseHW.get_humidity() > -1)
    assert(senseHW.get_humidity() < 101)

def test_getPressure():
    assert(senseHW.get_pressure() >= 0)
    assert(senseHW.get_pressure() < 1300)






