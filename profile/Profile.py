from lib.toolkit import load_properties


class Profile:
    properties_URI="conf/profile.properties"
    properties=""

    def __init__(self):
        self.properties = load_properties(self.properties_URI)

    def get_str_property(self, name):
        return self.properties[name]

    def get_int_property(self, name):
        return int(self.properties[name])