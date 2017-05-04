from lib.toolkit import log, load_properties
profile = load_properties("conf/profile.properties")

# 364 is submerged in water and 1024 is dry
from hw.sensor.AnalogSensor import AnalogSensor

soil_sensor = AnalogSensor(0, 1024, 364)
soil_sensor.get_value()
