import gc

from lib.toolkit import log


class Board:
    pin_mapping = []
    button_click_counter = {}

    def __init__(self, pin_mapping):
        self.pin_mapping = pin_mapping

    def get_pin_mapping(self):
        return self.pin_mapping

    def set_pin_mapping(self, pin_mapping):
        self.pin_mapping = pin_mapping

    def get_pin(self, pin_key):
        return self.pin_mapping[pin_key]

    def set_pin(self, pin_key, pin_value):
        self.pin_mapping[pin_key] = pin_value

    def get_pin_value(self, pin):
        return pin.value()

    def scan_wifi(self, mode):
        import network

        n = network.WLAN(mode)

        return n.scan()

    def connect_to_wifi(self, ssid, password, mode, wait_for_ip=0):
        import network, time

        log.info("Attempting to connect to WiFi '" + ssid + "' with password '" + password + "'...")
        n = network.WLAN(mode)
        n.active(True)
        n.connect(ssid, password)

        # Wait for IP address to be provided
        count = 0
        while not n.isconnected() and count < wait_for_ip:
            log.info("Waiting to obtain IP ... (" + str(wait_for_ip - count) + " sec remaining)")
            time.sleep(1)
            count += 1

        # Get provided IP
        ip = n.ifconfig()[0]

        if ip == "0.0.0.0":
            log.info("Could not obtain IP on '" + ssid + "'")
        else:

            log.info("Connected with IP '" + ip + "'")

        return ip

    def blink_onboard_led(self, times, delay, led):
        import time

        # Do blinking
        for i in range(times):
            led.high()
            time.sleep(delay)
            led.low()
            time.sleep(delay)

        # Return to off state
        led.high()

    def get_onboard_button_events(self, btn, bcc_key):
        from machine import Timer

        if btn.value() == 0:
            self.button_click_counter[bcc_key] += 1
            if self.button_click_counter[bcc_key] == 1:
                log.info("single-click registered (mem free: " + str(gc.mem_free()) + ")")
            elif self.button_click_counter[bcc_key] == 2:
                log.info("double click registered (mem free: " + str(gc.mem_free()) + ")")
            else:
                log.info("lots of clicks! (mem free: " + str(gc.mem_free()) + ")")

            gtim = Timer(1)
            gtim.init(period=300, mode=Timer.ONE_SHOT, callback=lambda t:self.reset_onboard_button_event_counter(bcc_key))

    def reset_onboard_button_event_counter(self, bcc_key):
        log.info("FBC resetting to 0. Previous was " + str(self.button_click_counter[bcc_key]))
        self.button_click_counter[bcc_key] = 0
        return self.button_click_counter[bcc_key]

    def format(self):
        import uos
        log.info("Formatting filesystem ...")

        while uos.listdir("/"):
            lst = uos.listdir("/")
            uos.chdir("/")
            while lst:
                try:
                    uos.remove(lst[0])
                    log.info("Removed '" + uos.getcwd() + "/" + lst[0] + "'")
                    lst = uos.listdir(uos.getcwd())
                except:
                    dir = lst[0]
                    log.info("Directory '" + uos.getcwd() + "/" + dir + "' detected. Opening it...")
                    uos.chdir(dir)
                    lst = uos.listdir(uos.getcwd())
                    if len(lst) == 0:
                        log.info("Directory '" + uos.getcwd() + "' is empty. Removing it...")
                        uos.chdir("..")
                        uos.rmdir(dir)
                        break

        log.info("Format completed successfully")


