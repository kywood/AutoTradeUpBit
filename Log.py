import logging
import logging.config
from enum import Enum


class eLogType(Enum):
    DEBUG=0
    INFO=1
    WARNING=2
    ERROR=3
    CRITICAL=4

    pass

class Log:

    def __init__(self,_name="",_configFile='logging.conf'):
        logging.config.fileConfig(_configFile)
        self.logger = logging.getLogger(_name)
        pass

    def Print(self,logType,message):

        if logType==eLogType.DEBUG :
            self.logger.debug(message)
        elif logType==eLogType.INFO :
            self.logger.info(message)
        elif logType==eLogType.WARNING :
            self.logger.warning(message)
        elif logType==eLogType.ERROR :
            self.logger.error(message)
        elif logType == eLogType.CRITICAL:
            self.logger.critical(message)
        else:
            self.logger.error(message)

        pass