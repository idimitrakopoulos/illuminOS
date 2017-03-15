class TemperatureUnit:
    CELSIUS = 0
    FAHRENHEIT = 1

    def __init__(self):
        pass

    def get_unit_initial(self, unit):
        result = "C"
        if unit == self.FAHRENHEIT:
            result = "F"
        return result

class HumidityUnit:
    PERCENT = 0

    def __init__(self):
        pass

    def get_unit_initial(self):
        return "%"


class PressureUnit:
    HECTOPASCAL = 0

    def __init__(self):
        pass

    def get_unit_initial(self, unit):
        result = "hPa"
        return result


class AltitudeUnit:
    METERS = 0

    def __init__(self):
        pass

    def get_unit_initial(self, unit):
        result = "m"
        return result