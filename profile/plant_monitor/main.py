from hw.board.NodeMCU import NodeMCU
import machine
from hw.screen.SSD1306 import SSD1306
from hw.screen.Screen import ConnectionType
from lib.PropertyManager import PropertyManager
from lib.toolkit import log, send_instapush_notification, determine_preferred_wifi, load_properties
from hw.sensor.AnalogSensor import AnalogSensor


if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    log.info("Woke from deep sleep ...")
else:
    log.info("Power on from hard reset ...")

p = PropertyManager("conf/profile.properties")
board = NodeMCU()

log.debug("Connecting to soil humidity sensor at pin {}".format(p.get_str_property("analog_pin")))

# SUBMERGED IN WATER (vlow)   : 364
# COMPLETELY DRY     (vhigh)  : 1024
soil_sensor = AnalogSensor(p.get_int_property("analog_pin"),
                           p.get_int_property("vhigh"),
                           p.get_int_property("vlow"))

# SSD1306 OLED init
log.debug("Connecting to SSD1306 OLED Screen at scl: {}, sda: {}".format(p.get_str_property("ssd1306_scl"),
                                                                         p.get_str_property("ssd1306_sda")))
bus = machine.I2C(freq=400000,
                  scl=machine.Pin(p.get_int_property("ssd1306_scl")),
                  sda=machine.Pin(p.get_int_property("ssd1306_sda")))

oled = SSD1306(ConnectionType.I2C, bus)


log.info("Soil humidity sensor value is {}".format(soil_sensor.get_value()))
oled.text("Soil Humidity")
oled.text("{}".format(soil_sensor.get_value()), 0, 10)

preferred_wifi = determine_preferred_wifi(load_properties("conf/network.properties"), board.scan_wifi())
ip = board.connect_to_wifi(preferred_wifi["ssid"], preferred_wifi["password"], 10)


lala= {'string': 'ssss'}

send_instapush_notification("5910caeaa4c48a63f7d2c9f9", "dde6406d08e0e88e6f3d71acb1c2ecde", "generic", lala)

# Wake every 8 hours a.k.a 3 times/day
# board.sleep(28800000)
board.sleep(5000)