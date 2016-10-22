import sys
import micropython
import hardware.node_mcu as board
from lib.toolkit import log, load_properties, scan_wifi, determine_preferred_wifi, connect_to_wifi


micropython.alloc_emergency_exception_buf(100)

# Startup heartbeat
board.blink_blue_led(15, 0.06)

# Print version
version_info = load_properties("MANIFEST.MF")
log.info(version_info["name"] + " " + version_info["version"] + " running on "  + sys.platform)


# Connect to WiFi
configured_wifis = load_properties("conf/network.properties")
found_wifis = scan_wifi()
preferred_wifi = determine_preferred_wifi(configured_wifis, found_wifis)
ip = connect_to_wifi(preferred_wifi["ssid"], preferred_wifi["password"], 10)


# hardware.get_flash_button_interrupts()
# hardware.get_user_button_interrupts()


