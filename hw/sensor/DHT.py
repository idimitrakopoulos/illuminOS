import dht

from lib.toolkit import log, find_enum_id


class DHT:
    type_mapping = ""
    unit_mapping = ""
    type = ""
    sensor = ""


    # @timed_function
    def __init__(self, type, pin):
        self.type_mapping = list(enumerate(['DHT11', 'DHT22']))
        self.unit_mapping = list(enumerate(['C', 'F']))
        self.type = find_enum_id(self.type_mapping, type)

        if find_enum_id(self.type_mapping, type) == 0:
            self.sensor = dht.DHT11(pin)
        elif find_enum_id(self.type_mapping, type) == 1:
             self.sensor = dht.DHT22(pin)
        else:
            log.error("Unknown sensor type '" + type + "'. Cannot instantiate it.")

    # @timed_function
    def get_temperature(self, unit="C", show_unit=True):
        self.sensor.measure()
        result = self.sensor.temperature() if unit=="C" else self.convert_C_to_F("%.2f" % self.sensor.temperature())
        if show_unit :
            result = str(result) + unit
        return result

    # @timed_function
    def get_humidity(self, unit="%", show_unit=True):
        self.sensor.measure()
        result = self.sensor.humidity()
        if show_unit:
            result = str(result) + unit
        return result

    # @timed_function
    def convert_C_to_F(self, celsius):
        return (float(celsius) * 9 / 5) + 32