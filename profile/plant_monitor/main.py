from lib.toolkit import log
from profile.Profile import Profile

p = Profile()

# 364 is submerged in water and 1024 is dry
from hw.sensor.AnalogSensor import AnalogSensor

log.debug("Connecting to sensor at pin " + p.get_str_property("analog_pin") + ".")


soil_sensor = AnalogSensor(p.get_int_property("analog_pin"),
                           p.get_int_property("vhigh"),
                           p.get_int_property("vlow"))

# log.debug("Connecting to sensor at pin " + p.get_str_property("analog_pin") + ".")

soil_sensor.get_value()
