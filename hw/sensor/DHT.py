import dht

from lib.toolkit import log

class DHTType:
    DHT11 = 0
    DHT22 = 1

    def __init__(self):
        pass

class TemperatureUnit:
    CELSIUS = 0
    FAHRENHEIT = 1

    def __init__(self):
        pass

    def get_unit_initial(self, unit):
        result = "C"
        if unit == self.FAHRENHEIT:
            result = "F"
        return result

class HumidityUnit:
    PERCENT = 0

    def __init__(self):
        pass

    def get_unit_initial(self):
        return "%"

class DHT:
    type = ""
    sensor = ""


    # @timed_function
    def __init__(self, type, pin):
        self.type = type

        if self.type == 0:
            self.sensor = dht.DHT11(pin)
        elif self.type == 1:
             self.sensor = dht.DHT22(pin)
        else:
            log.error("Unknown sensor type '" + self.type + "'. Cannot instantiate it.")

    # @timed_function
    def get_temperature(self, unit=TemperatureUnit.CELSIUS, show_unit=False):
        self.sensor.measure()
        result = self.sensor.temperature() if unit == TemperatureUnit.CELSIUS else self.convert_C_to_F("%.2f" % self.sensor.temperature())
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

    # @timed_function
    def convert_C_to_F(self, celsius):
        return (float(celsius) * 9 / 5) + 32