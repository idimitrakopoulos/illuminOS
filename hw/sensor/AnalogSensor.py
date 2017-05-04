import machine

class AnalogSensor:
    sensor = ""
    vhigh = 0
    vlow = 0


    # @timed_function
    def __init__(self, pin, vhigh, vlow):
        self.sensor = machine.ADC(pin)
        self.vhigh = vhigh
        self.vlow = vlow

    def get_value(self):
        return self.sensor.read()

    def get_low(self):
        return self.vlow

    def get_high(self):
        return self.vhigh