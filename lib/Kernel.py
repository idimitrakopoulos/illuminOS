from lib.Logger import Logger
import micropython

class Kernel:

    os_properties = []
    logger = ""

    def __init__(self, os_properties):
        # Read OS properties
        self.os_properties = os_properties
        micropython.alloc_emergency_exception_buf(100)

        # Logger
        self.logger = Logger(self.os_properties['log_level'])



