from lib.Logger import Logger

class Kernel:

    os_properties = []
    logger = ""

    def __init__(self, os_properties):
        # Read OS properties
        self.os_properties = os_properties

        # Logger
        self.logger = Logger(self.os_properties['log_level'])



