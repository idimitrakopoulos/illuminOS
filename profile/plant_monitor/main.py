from lib.toolkit import log, load_properties
props = load_properties("conf/profile.properties")

# 364 is submerged in water and 1024 is dry
from hw.sensor.AnalogSensor import AnalogSensor

soil_sensor = AnalogSensor(int(props["analog_pin"]), int(props["vhigh"]), int(props["vlow"]))
soil_sensor.get_value()
