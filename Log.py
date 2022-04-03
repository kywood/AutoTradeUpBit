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

    def __init__(self,_name="",_configFile='logging.conf',_version=""):
        logging.config.fileConfig(_configFile)
        self.logger = logging.getLogger(_name)
        self.version=_version
        pass

    def Print(self,logType,message):

        nmes = f"""[{self.version}] {message}"""

        if logType==eLogType.DEBUG :
            self.logger.debug(nmes)
        elif logType==eLogType.INFO :
            self.logger.info(nmes)
        elif logType==eLogType.WARNING :
            self.logger.warning(nmes)
        elif logType==eLogType.ERROR :
            self.logger.error(nmes)
        elif logType == eLogType.CRITICAL:
            self.logger.critical(nmes)
        else:
            self.logger.error(nmes)

        pass