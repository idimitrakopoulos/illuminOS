class ScreenType:
    SSD1306 = 0
    SSD1106 = 1

    def __init__(self):
        pass

class ConnectionType:
    I2C = 0
    SPI = 1

    def __init__(self):
        pass


class Screen:
    type = ""
    connection_type = ""


    # @timed_function
    def __init__(self, screen_type, connection_type, pins):
        self.type = screen_type
        self.connection_type = connection_type


