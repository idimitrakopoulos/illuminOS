from hw.screen.Screen import Screen, ScreenType
import time, ssd1306
from toolkit import log


class SSD1306(Screen):

    def __init__(self, connection_type, bus):
        Screen.__init__(self, ScreenType.SSD1306, connection_type, bus)

        if self.connection_type == 0:
            self.screen = ssd1306.SSD1306_I2C(128, 32, self.bus)
            self.screen.fill(0)

            # do a little optional visible init to show that the screen is ready
            self.init_screen(self.screen)

        else:

            log.error("Unknown screen connection type '" + self.connection_type + "'. Cannot instantiate it.")

    def text(self, string, x, y):
        self.screen.text(string, x, y)
        self.screen.show()

    def init_screen(self, oled):
        oled.invert(1)
        oled.text("init OK", 0, 10)
        oled.show()
        time.sleep(1)
        oled.invert(0)
        oled.fill(0)
        oled.show()


    def scroll_down_show(self, oled, line_to_show):

        for y in range(0, -6, -1):
            time.sleep(0.01)
            oled.scroll(0, y)

            if y == -5:
                oled.text(line_to_show, 0, 15)
            oled.show()


    # def scroll_right_show(self, oled, line_to_show):
    #     for x in range(0, -6, -1):
    #         time.sleep(0.01)
    #         oled.scroll(x, 0)
    #
    #         if x == -5:
    #             oled.text(line_to_show, 15, 0)
    #         oled.show()
