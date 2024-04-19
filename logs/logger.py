import os.path


class Logger:
    def __init__(self, baseDir):
        self.baseDir = baseDir

    def debug(self, message):
        debug = open(os.path.join(self.baseDir, 'debug'), 'w')
        debug.write(message)
        debug.close()
