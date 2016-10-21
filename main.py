from util.toolkit import format_fs, log, load_properties, scan_wifi, determine_preferred_wifi, connect_to_wifi, sendInstapushNotification
import sys
import util.nodemcu as board
import micropython

micropython.alloc_emergency_exception_buf(100)

board.blink_blue_led(15, 0.06)

version_info = load_properties("MANIFEST.MF")
log(version_info["name"] + " " + version_info["version"] + " running on "  + sys.platform)



configured_wifis = load_properties("conf/network.properties")
found_wifis = scan_wifi()
preferred_wifi = determine_preferred_wifi(configured_wifis, found_wifis)
ip = connect_to_wifi(preferred_wifi["ssid"], preferred_wifi["password"])

log("Connected with IP: " + ip)



# board.get_flash_button_interrupts()
# board.get_user_button_interrupts()
