import time

import machine
import ssd1306
from hw.sensor.bmp180.bmp180 import BMP180
from machine import I2C, Pin

from hw.board.NodeMCU import NodeMCU
from lib.PropertyManager import PropertyManager
from lib.toolkit import log

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    log.info("Woke from deep sleep ...")
else:
    log.info("Power on from hard reset ...")

p = PropertyManager()
board = NodeMCU()

# BMP180 init
bus =  I2C(scl=Pin(p.get_int_property("bmp_scl")),
           sda=Pin(p.get_int_property("bmp_sda")),
           freq=100000)

bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

# OLED init
i2c = machine.I2C(machine.Pin(p.get_int_property("ssd1306_scl")),
                  machine.Pin(p.get_int_property("ssd1306_sda")))

oled = ssd1306.SSD1306_I2C(p.get_int_property("ssd1306_x_pixels"),
                           p.get_int_property("ssd1306_x_pixels"),
                           i2c)

while True:
    temperature = bmp180.temperature
    pressure = bmp180.pressure
    altitude = bmp180.altitude


    oled.fill(0)
    oled.text('Temp : ' + str(("%.1f" % temperature)) + "C", 0, 0)
    oled.text('Press: ' + str(("%.2f" % (pressure / 100))) + "hPa", 0, 10)
    oled.text('Alt  : ' + str(("%.2f" % altitude)) + "m", 0, 20)
    oled.show()


    # print(("%.1f" % temperature), ("%.2f" % (pressure / 100)), ("%.2f" % altitude))
    time.sleep(5)


# Wake every 8 hours a.k.a 3 times/day
# board.sleep(28800000)
# board.sleep(5000)

