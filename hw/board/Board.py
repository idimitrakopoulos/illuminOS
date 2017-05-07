import lib.toolkit as tk
from lib.toolkit import log


class Board:
    pin_mapping = []
    button_click_counter = {}

    # @timed_function
    def __init__(self, pin_mapping):
        self.pin_mapping = pin_mapping

    # @timed_function
    def get_pin_mapping(self):
        return self.pin_mapping

    # @timed_function
    def set_pin_mapping(self, pin_mapping):
        self.pin_mapping = pin_mapping

    # @timed_function
    def get_pin_by_key(self, pin_key):
        return self.pin_mapping[pin_key]

    # @timed_function
    def set_pin(self, pin_key, pin):
        self.pin_mapping[pin_key] = pin

    # @timed_function
    def get_pin_value(self, pin):
        return pin.value()

    # @timed_function
    def scan_wifi(self, mode):
        import network

        n = network.WLAN(mode)

        return n.scan()

    # @timed_function
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

    # @timed_function
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

    # @timed_function
    def get_onboard_button_events(self, btn, bcc_key, on_single_click, on_double_click):
        import gc
        from machine import Timer

        if btn.value() == 0:
            self.button_click_counter[bcc_key] += 1
            if self.button_click_counter[bcc_key] == 1:
                log.info("single-click registered (mem free: " + str(gc.mem_free()) + ")")
                sc = getattr(tk, on_single_click)
                sc()

            elif self.button_click_counter[bcc_key] == 2:
                log.info("double click registered (mem free: " + str(gc.mem_free()) + ")")
                sc = getattr(tk, on_double_click)
                sc()
            else:
                pass

            gtim = Timer(1)
            gtim.init(period=300, mode=Timer.ONE_SHOT, callback=lambda t:self.reset_onboard_button_event_counter(bcc_key))

    # @timed_function
    def reset_onboard_button_event_counter(self, bcc_key):
        log.info("FBC resetting to 0. Previous was " + str(self.button_click_counter[bcc_key]))
        self.button_click_counter[bcc_key] = 0
        return self.button_click_counter[bcc_key]

    # @timed_function
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


    def start_memory_manager(self, period=5000):
        from machine import Timer

        tim = Timer(0)
        tim.init(period=period, mode=Timer.PERIODIC, callback=lambda t: self.mem_cleanup())


    def mem_cleanup(self):
        import gc
        log.debug("Invoking garbage collection ...")
        gc.collect()
        mem = gc.mem_free()
        if 6001 <= mem <= 10000:
            log.warn("Memory is low: " + str(mem))
        elif 4001 <= mem <= 6000:
            log.warn("Memory is very low: " + str(mem))
        elif mem < 4000:
            log.critical("Memory is extremely low: " + str(mem))
        else:
            log.debug("Memory is currently: " + str(mem))


    def get_public_ip(self):
        from lib.toolkit import http_get
        """
        This is a rather hacky way to get the external IP
        but it avoids importing urequests module which is heavy on mem usage.
        """
        s = http_get("http://myexternalip.com/raw")
        ip = ""
        for x in range(0, 10):
            ip = (s.readline().decode('ascii')).strip("\n")

        return ip

    def sleep(self, milliseconds):
        # To be able to use this fea
        import machine

        # configure RTC.ALARM0 to be able to wake the device
        rtc = machine.RTC()
        rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

        # set RTC.ALARM0 to fire after some milliseconds
        rtc.alarm(rtc.ALARM0, milliseconds)

        # put the device to sleep
        machine.deepsleep()