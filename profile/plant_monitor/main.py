from hw.board.NodeMCU import NodeMCU
from lib.toolkit import log
from profile.Profile import Profile
import machine

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    log.info("Woke from deep sleep ...")
else:
    log.info("Power on from hard reset ...")

p = Profile()
board = NodeMCU()

from hw.sensor.AnalogSensor import AnalogSensor

log.debug("Connecting to soil humidity sensor at pin {}".format(p.get_str_property("analog_pin")))

# SUBMERGED IN WATER (vlow)   : 364
# COMPLETELY DRY     (vhigh)  : 1024
soil_sensor = AnalogSensor(p.get_int_property("analog_pin"),
                           p.get_int_property("vhigh"),
                           p.get_int_property("vlow"))

log.info("Soil humidity sensor value is {}".format(soil_sensor.get_value()))


# Wake every 8 hours a.k.a 3 times/day
# board.sleep(28800000)
board.sleep(5000)
