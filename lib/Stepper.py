# from lib.toolkit import log
from lib.PropertyManager import PropertyManager


class Stepper:
    pstep_properties = ""
    steps = 0
    current_step = 0

    def __init__(self, uri, steps):
        self.steps = steps
        try:
            self.pstep_properties = PropertyManager(uri)
            self.current_step = self.pstep_properties.get_int_property("current_step")
            # log.debug("Previous step file found at '{}'".format(uri))
        except:
            self.current_step = 1
            # log.debug("Previous step file not found at '{}'. Assuming this is the first step.".format(uri))


    def get_current_step(self):
        return self.current_step



