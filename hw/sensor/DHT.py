import dht
from machine import Pin

from lib.Unit import TemperatureUnit, HumidityUnit
from lib.toolkit import log, convert_C_to_F


class DHTType:
    DHT11 = 0
    DHT22 = 1

    def __init__(self):
        pass

class DHT:
    type = ""
    sensor = ""


    # @timed_function
    def __init__(self, type, pin):
        self.type = type

        if self.type == 0:
            self.sensor = dht.DHT11(Pin(pin))
        elif self.type == 1:
             self.sensor = dht.DHT22(Pin(pin))
        else:
            log.error("Unknown sensor type '" + self.type + "'. Cannot instantiate it.")

    # @timed_function
    def get_temperature(self, unit=TemperatureUnit.CELSIUS, show_unit=False):
        self.sensor.measure()
        result = self.sensor.temperature() if unit == TemperatureUnit.CELSIUS else convert_C_to_F("%.1f" % self.sensor.temperature())
        if show_unit :
            result = str(result) + TemperatureUnit.get_unit_initial(TemperatureUnit(), unit)
        return result

    # @timed_function
    def get_humidity(self, unit=HumidityUnit.get_unit_initial(HumidityUnit()), show_unit=False):
        self.sensor.measure()
        result = self.sensor.humidity()
        if show_unit:
            result = str(result) + unit
        return result

