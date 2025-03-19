import logging.config
import os


class Log(object):
    def __init__(self):
        logging.config.fileConfig(os.path.dirname(__file__) + "/logging.conf")
        self.logger = logging.getLogger()
