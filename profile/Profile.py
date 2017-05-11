from lib.toolkit import load_properties, log


class Profile:
    properties_URI="conf/profile.properties"
    properties=""

    def __init__(self):
        self.properties = load_properties(self.properties_URI)
        log.info("Using profile '{}'".format(self.get_str_property("name")))

    def get_str_property(self, name):
        return self.properties[name]

    def get_int_property(self, name):
        return int(self.properties[name])