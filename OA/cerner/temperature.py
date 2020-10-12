"""
Design a temperature class dealing with temperature, 
and how do distinguish when someone has a fever or their temperature is higher than normal. 

How would you design an object to send an alert if a patient has a fever, given temperature readings every few minutes? 
Design a Temp Class which takes input as C, F or K and also consider the part of body from which temp is measured. 

Give a result through a method whether the patient has fever or not. 
Track patients fever in every one hour and create a report based on the analysis. 
Construct a class for Person Demographics. 

What kind of data types you use? 
Was asked to design a Temperature class for recording Temp for every hour (Used a circular queue which the interviewer liked ) 

a question about log case situation having thread id and process id( glass door has the question posted can refer it if needed) , Was asked to write a scheduler method for the told class , it was a difficult question as they are expecting us to know the calender and date class

"""

from enum import Enum


class Location(Enum):
    MOUTH, EAR, ARMPIT = 0, 1, 2


class TemperatureUnit(Enum):
    FAHRENHEIT, CELSIUS, KELVIN = 1, 2, 3


class Temperature:
    def __init__(self, temperature_unit: TemperatureUnit):
        self.temperature_unit = temperature_unit
        self.temperatures = [[float('inf'), 0] for _ in range(len(Location))]

    def get_temperatures(self):
        return self.temperatures

    def set_temperature_unit(self, temperature_unit: TemperatureUnit):
        self.temperature_unit = temperature_unit

    def test_temperature(self, location: Location, temperature: float):
        idx = location.value
        degree = self.temperatures[idx]
        self.temperatures[idx][0] = min(degree[0], temperature)
        self.temperatures[idx][1] = max(degree[1], temperature)

    def is_fever(self):
        for location in Location:
            idx = location.value
            degree = self.temperatures[idx]
            celsius = self.get_celsius(degree[1])
            threshold = self.get_fever_threshold(location)
            if celsius > threshold:
                return True
        
        return False

    def get_fever_threshold(self, location):
        if location == Location.MOUTH:
            return 38
        elif location == Location.ARMPIT:
            return 38
        elif location == Location.EAR:
            return 38

    def get_celsius(self, temperature):
        if self.temperature_unit == TemperatureUnit.CELSIUS:
            return temperature
        elif self.temperature_unit == TemperatureUnit.FAHRENHEIT:
            return (temperature - 32) * 5/9
        elif self.temperature_unit == TemperatureUnit.KELVIN:
            return temperature - 273.15


t = Temperature(TemperatureUnit.FAHRENHEIT)
t.test_temperature(Location.EAR, 99)
t.test_temperature(Location.EAR, 90)
print(t.get_temperatures())
print(t.is_fever())
