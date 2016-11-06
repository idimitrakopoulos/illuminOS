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
from hw.NodeMCU import NodeMCU

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