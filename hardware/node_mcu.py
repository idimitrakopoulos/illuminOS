import machine

GPIO0   = 0
GPIO1   = 1
GPIO2   = 2
GPIO15  = 15
GPIO16  = 16


blue_led        = machine.Pin(GPIO2, machine.Pin.OUT)
# red_led         = machine.Pin(GPIO15, machine.Pin.OUT)
user_button     = machine.Pin(GPIO16, machine.Pin.IN)
flash_button    = machine.Pin(GPIO0, machine.Pin.IN)

def blink_blue_led(times, delay):
    import lib.toolkit
    lib.toolkit.blink_onboard_led(times, delay, blue_led)


def get_flash_button_interrupts():
    from machine import Timer
    from lib.toolkit import get_button_clicks, button_click_counter

    button_click_counter['flash'] = 0

    tim = Timer(0)
    tim.init(period=200, mode=Timer.PERIODIC, callback=lambda t: get_button_clicks(flash_button, 'flash'))


def get_user_button_interrupts():
    from machine import Timer
    from lib.toolkit import get_button_clicks, button_click_counter

    button_click_counter['user'] = 0

    tim = Timer(1)
    tim.init(period=200, mode=Timer.PERIODIC, callback=lambda t: get_button_clicks(user_button, 'user'))