from lib.toolkit import log
from lib.PropertyManager import PropertyManager


class Stepper:
    prop_manager = None
    steps = 0
    current_step = 0

    def __init__(self, uri, steps):
        self.steps = steps
        try:
            self.prop_manager = PropertyManager(uri)
            self.current_step = self.prop_manager.get_int_property("current_step")
            log.debug("Previous step file found at '{}'".format(uri))
        except:
            self.current_step = 1
            log.debug("Previous step file not found at '{}'. Assuming this is the first step.".format(uri))


    def get_current_step(self):
        return self.current_step


    def create_property_file(self, uri, dict):
        try:
            with open(uri, "w") as f:
                for key, value in dict.items():
                    f.write(str(key) + " = " + str(value) + "\n")

        except OSError:
            log.warn("Can't write to file %s" % uri)

        finally:
            f.close()


    def remove_property_file(self, uri):
        import uos
        uos.remove(uri)