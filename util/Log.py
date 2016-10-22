class Log:

    def __init__(self):
        self.log_levels = list(enumerate(['INFO', 'DEBUG', 'WARN', 'ERROR', 'CRITICAL', 'FATAL']))

    def log(self, msg, level=0):
        print("[" + self.log_levels[level][1] + "] " + str(msg))

    def info(self, msg):
        print("[" + self.log_levels[0][1] + "] " + str(msg))

    def debug(self, msg):
        print("[" + self.log_levels[1][1] + "] " + str(msg))

    def warn(self, msg):
        print("[" + self.log_levels[2][1] + "] " + str(msg))

    def error(self, msg):
        print("[" + self.log_levels[3][1] + "] " + str(msg))

    def critical(self, msg):
        print("[" + self.log_levels[4][1] + "] " + str(msg))

    def fatal(self, msg):
        print("[" + self.log_levels[5][1] + "] " + str(msg))