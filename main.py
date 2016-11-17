import sys

from hw.board.NodeMCU import NodeMCU
from lib.toolkit import log, load_properties, determine_preferred_wifi

# Instantiate our board
board = NodeMCU()

# Startup heartbeat
board.blink_blue_led(8, 0.04)

# Print version
version_info = load_properties("MANIFEST.MF")
log.info(version_info["name"] + " " + version_info["version"] + " running on "  + sys.platform)


# Connect to WiFi
preferred_wifi = determine_preferred_wifi(load_properties("conf/network.properties"), board.scan_wifi())
ip = board.connect_to_wifi(preferred_wifi["ssid"], preferred_wifi["password"], 10)


from hw.sensor.DHT import DHT, DHTType, TemperatureUnit
import machine

# Instantiate our sensor
d = DHT(DHTType.DHT11, machine.Pin(10))

# Get temperature in Celsius
d.get_temperature()

# Get temperature in Fahrenheit
d.get_temperature(TemperatureUnit.FAHRENHEIT)

