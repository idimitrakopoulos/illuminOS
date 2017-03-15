# ----------------------------------------------------------------------------------------------------------------------
#
# Generic Examples
#
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Initialize OS
# ----------------------------------------------------------------------------------------------------------------------
from lib.Kernel import Kernel
from lib.toolkit import load_properties, determine_preferred_wifi
# Start-up Kernel
kernel = Kernel(load_properties("conf/os.properties"))
log = kernel.logger

# ----------------------------------------------------------------------------------------------------------------------
# Logger
# ----------------------------------------------------------------------------------------------------------------------
import gc
from lib.Logger import Logger
log = Logger("DEBUG")

log.info("Hello!")
log.error("Critical Issue!!")
log.debug("Free memory: " + str(gc.mem_free()))

# ----------------------------------------------------------------------------------------------------------------------
# Update DuckDNS
# ----------------------------------------------------------------------------------------------------------------------
from lib.toolkit import update_duck_dns

# Update DuckDNS service
update_duck_dns("mydomain", "mytoken", "myip")

# ----------------------------------------------------------------------------------------------------------------------
#
# NodeMCU Examples
#
# ----------------------------------------------------------------------------------------------------------------------
from hw.board.NodeMCU import NodeMCU

# ----------------------------------------------------------------------------------------------------------------------
# Connect to user preferred WiFi
# ----------------------------------------------------------------------------------------------------------------------
# Instantiate our board
board = NodeMCU()

# Find preferred wifi
preferred_wifi = determine_preferred_wifi(load_properties("conf/network.properties"), board.scan_wifi())

# Get IP
ip = board.connect_to_wifi(preferred_wifi["ssid"], preferred_wifi["password"], 10)

# ----------------------------------------------------------------------------------------------------------------------
# Button event listener
# ----------------------------------------------------------------------------------------------------------------------
# Instantiate our board
board = NodeMCU()

# Listen for events on FLASH button and run "hello_world" function on single and double click
board.get_flash_button_events("hello_world", "hello_world")

# Listen for events on USER button and run "hello_world" function on single and double click
board.get_user_button_events("hello_world", "hello_world")


# ----------------------------------------------------------------------------------------------------------------------
# LED blinking
# ----------------------------------------------------------------------------------------------------------------------
# Instantiate our board
board = NodeMCU()

# Blink BLUE LED 5 times with 0.5 sec delay
board.blink_blue_led(5, 0.5)

# ----------------------------------------------------------------------------------------------------------------------
# Format Filesystem
# ----------------------------------------------------------------------------------------------------------------------
# Instantiate our board
board = NodeMCU()

# Request format - this will wipe all the filesystem
board.format()

  # ----------------------------------------------------------------------------------------------------------------------
# Start Memory Manager
# ----------------------------------------------------------------------------------------------------------------------
# Instantiate our board
board = NodeMCU()

# Memory collection and reporting will occur every 10 sec
board.start_memory_manager(10000)

# Or you can run memory manager ad hoc
board.mem_cleanup()


# ----------------------------------------------------------------------------------------------------------------------
# Drive Humidity/Temperature sensor (DHT11 or DHT22)
# ----------------------------------------------------------------------------------------------------------------------
from hw.sensor.DHT import DHT, DHTType, TemperatureUnit

# Instantiate our sensor
d = DHT(DHTType.DHT11, 10)

# Get temperature in Celsius
d.get_temperature()

# Get temperature in Fahrenheit
d.get_temperature(TemperatureUnit.FAHRENHEIT)

# Get temperature numeric in Celsius
d.get_temperature(TemperatureUnit.CELSIUS, False)

# Get temperature numeric in Fahrenheit
d.get_temperature(TemperatureUnit.FAHRENHEIT, False)


# ----------------------------------------------------------------------------------------------------------------------
# Drive Temperature/Pressure/Altitude sensor (BMP180 or BMP280)
# ----------------------------------------------------------------------------------------------------------------------
from hw.sensor.BMP import BMP, BMPType, TemperatureUnit, PressureUnit, AltitudeUnit

# Instantiate our sensor
s = BMP(BMPType.BMP180, 2, 0)

# Get temperature in Celsius
s.get_temperature()

# Get temperature in Fahrenheit
s.get_temperature(TemperatureUnit.FAHRENHEIT)

# Get temperature numeric in Celsius
s.get_temperature(TemperatureUnit.CELSIUS, False)

# Get temperature numeric in Fahrenheit
s.get_temperature(TemperatureUnit.FAHRENHEIT, False)

# Get altitude in meters
s.get_altitude(AltitudeUnit.METERS)

# Get pressure in hectopascals
s.get_pressure(PressureUnit.HECTOPASCAL)

# ----------------------------------------------------------------------------------------------------------------------
# Drive SSD1306 Display with I2C connection
# ----------------------------------------------------------------------------------------------------------------------
from hw.screen.SSD1306 import SSD1306
from hw.screen.Screen import ConnectionType
import machine

bus = machine.I2C(machine.Pin(4), machine.Pin(5))

oled = SSD1306(ConnectionType.I2C, bus)

