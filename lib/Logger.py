class Logger:

    log_levels = []
    log_level_id = 1 # DEBUG

    def __init__(self, log_level):
        self.log_levels = list(enumerate(['TRACE', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL', 'OFF']))
        self.log_level_id = self.find_log_level_id(log_level)
        self.debug("Logging level set to '" + log_level + "' (" + str(self.log_level_id) + ")")

    def find_log_level_id(self, log_level):
        result = 0
        for i in self.log_levels:
            if i[1] == log_level:
                result = i[0]

        return result

    def trace(self, msg):
        if self.log_level_id == 0:
            print("[" + self.log_levels[0][1] + "] " + str(msg))

    def debug(self, msg):
        if self.log_level_id <= 1:
            print("[" + self.log_levels[1][1] + "] " + str(msg))

    def info(self, msg):
        if self.log_level_id <= 2:
            print("[" + self.log_levels[2][1] + "] " + str(msg))

    def warn(self, msg):
        if self.log_level_id <= 3:
            print("[" + self.log_levels[3][1] + "] " + str(msg))

    def error(self, msg):
        if self.log_level_id <= 4:
            print("[" + self.log_levels[4][1] + "] " + str(msg))

    def fatal(self, msg):
        if self.log_level_id <= 5:
            print("[" + self.log_levels[5][1] + "] " + str(msg))
