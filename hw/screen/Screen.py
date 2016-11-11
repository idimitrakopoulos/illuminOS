from lib.toolkit import find_enum_id


class Screen:
    type_mapping = ""
    connection_type_mapping = ""
    type = ""
    connection_type = ""


    # @timed_function
    def __init__(self, type, connection_type, pins):
        self.type_mapping = list(enumerate(['OLED']))
        self.connection_type_mapping = list(enumerate(['I2C', 'SPI']))
        self.type = find_enum_id(self.type_mapping, type)
        self.connection_type = find_enum_id(self.connection_type_mapping, connection_type)


