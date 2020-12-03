import serverpi_humidity
import serverpi_temperature
import serverpi_pressure

if __name__ == "__main__":
    
    serverpi_humidity.pollHumidity()
    serverpi_temperature.pollTemperature()
    serverpi_pressure.pollPressure()