from lib.toolkit import load_properties

class PropertyManager:
    properties = None

    def __init__(self, uri):
        self.properties = load_properties(uri)


    def get_str_property(self, name):
        return self.properties[name]

    def get_int_property(self, name):
        return int(self.properties[name])

