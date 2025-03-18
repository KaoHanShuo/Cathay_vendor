import logging.config
import time
import os

class log(object):
    def __init__(self):
        logging.config.fileConfig(os.path.dirname(__file__) + "/logging.conf")
        self.logger = logging.getLogger()
        self.logger.info("driver 啟動成功")