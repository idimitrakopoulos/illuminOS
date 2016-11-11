from hw.screen.Screen import Screen


class SSD1306(Screen):

    def __init__(self, type, connection_type, pins):
        Screen.__init__(self, type, connection_type, pins)