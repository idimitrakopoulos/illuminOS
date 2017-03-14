from hw.screen.Screen import Screen
import time


class SSD1306(Screen):

    def __init__(self, type, connection_type, pins):
        Screen.__init__(self, type, connection_type, pins)


    def scroll_down_show(self, oled, line_to_show):

        for y in range(0, -6, -1):
            time.sleep(0.01)
            oled.scroll(0, y)

            if y == -5:
                oled.text(line_to_show, 0, 15)
            oled.show()
