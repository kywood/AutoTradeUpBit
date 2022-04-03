import time
import datetime


class Utils:


    @staticmethod
    # def CurrentTimeString(_format="""%Y%m%d-%H:%M:%S"""):
    def CurrentTimeString(_format="""%Y%m%d%H%M%S"""):
        return datetime.datetime.now().strftime(_format)