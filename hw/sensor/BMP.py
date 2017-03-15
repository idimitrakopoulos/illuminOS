from lib.bmp180.bmp180 import BMP180
from machine import I2C, Pin

from lib.Unit import TemperatureUnit, PressureUnit, AltitudeUnit
from lib.toolkit import log, convert_C_to_F


class BMPType:
    BMP180 = 0
    BMP280 = 1

    def __init__(self):
        pass

class BMP:
    type = ""
    sensor = ""


    # @timed_function
    def __init__(self, type, scl, sda):
        self.type = type

        if self.type == 0:
            i2c = I2C(scl=Pin(scl), sda=Pin(sda), freq=100000)
            self.sensor = BMP180(i2c)
            self.sensor.oversample_sett = 2
            self.sensor.baseline = 101325

        elif self.type == 1:
             pass #TODO

        else:
            log.error("Unknown sensor type '" + self.type + "'. Cannot instantiate it.")

    # @timed_function
    def get_temperature(self, unit=TemperatureUnit.CELSIUS, show_unit=False):
        result = self.sensor.temperature if unit == TemperatureUnit.CELSIUS else convert_C_to_F("%.1f" % self.sensor.temperature)
        if show_unit :
            result = str(result) + TemperatureUnit.get_unit_initial(TemperatureUnit(), unit)
        return result

    # @timed_function
    def get_pressure(self, unit=PressureUnit.HECTOPASCAL, show_unit=False):
        result = ("%.2f" % (self.sensor.pressure / 100))
        if show_unit:
            result = str(result) + PressureUnit.get_unit_initial(PressureUnit(), unit)
        return result

    # @timed_function
    def get_altitude(self, unit=AltitudeUnit.METERS, show_unit=False):
        result = ("%.2f" % self.sensor.pressure)
        if show_unit:
            result = str(result) + AltitudeUnit.get_unit_initial(AltitudeUnit(), unit)
        return result