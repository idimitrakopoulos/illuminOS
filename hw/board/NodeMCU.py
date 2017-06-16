import machine

from hw.board.Board import Board


class NodeMCU(Board):

    pins = {

        # "BTN_FLASH" :   machine.Pin(0, machine.Pin.IN),
        # "GPIO1"     :   machine.Pin(1, machine.Pin.IN),
        # "LED_BLUE"  :   machine.Pin(2, machine.Pin.OUT),
        # "GPIO3"     :   machine.Pin(3, machine.Pin.IN),
        # "GPIO4"     :   machine.Pin(4, machine.Pin.IN),
        # "GPIO5"     :   machine.Pin(5, machine.Pin.IN),
        # "GPIO12"    :   machine.Pin(12, machine.Pin.IN),
        # "GPIO13"    :   machine.Pin(13, machine.Pin.IN),
        # "GPIO14"    :   machine.Pin(14, machine.Pin.IN),
        # "GPIO15"    :   machine.Pin(15, machine.Pin.IN),
        # "BTN_USER"  :   machine.Pin(16, machine.Pin.IN),

    }

    def __init__(self):
        Board.__init__(self, self.pins)

    # @timed_function
    def blink_blue_led(self, times, delay):
        Board.blink_onboard_led(self, times, delay, self.get_pin_by_key("LED_BLUE"))

    # @timed_function
    def get_flash_button_events(self, on_single_click, on_double_click):
        from machine import Timer

        Board.button_click_counter['flash'] = 0

        pin = self.get_pin_by_key("BTN_FLASH")

        tim = Timer(0)
        tim.init(period=200, mode=Timer.PERIODIC, callback=lambda t: Board.get_onboard_button_events(self, pin, 'flash', on_single_click, on_double_click))

    # @timed_function
    def get_user_button_events(self, on_single_click, on_double_click):
        from machine import Timer

        Board.button_click_counter['user'] = 0

        pin = self.get_pin_by_key("BTN_USER")

        tim = Timer(0)
        tim.init(period=200, mode=Timer.PERIODIC, callback=lambda t: Board.get_onboard_button_events(self, pin, 'user', on_single_click, on_double_click))

    # @timed_function
    def scan_wifi(self):
        import network
        return Board.scan_wifi(self, network.STA_IF)

    # @timed_function
    def connect_to_wifi(self, ssid, password, wait_for_ip):
        import network
        return Board.connect_to_wifi(self, ssid, password, network.STA_IF, wait_for_ip)

