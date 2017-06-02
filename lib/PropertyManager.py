from lib.toolkit import load_properties

class PropertyManager:
    properties=""

    def __init__(self, uri):
        self.properties = load_properties(uri)

    def get_str_property(self, name):
        return self.properties[name]

    def get_int_property(self, name):
        return int(self.properties[name])

    def create_property_file(self, uri, dict):
        try:
            with open(uri, "w") as f:
                for key, value in dict.items():
                    f.write(str(key) + " = " + str(value) + "\n")

        except OSError:
            print("Can't write to file %s" % uri)

        finally:
            f.close()

    def remove_property_file(self, uri):
        import uos
        uos.remove(uri)