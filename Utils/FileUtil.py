import os
import sys

from Utils.FileWriter import FileWriter


class FileUtil(FileWriter):

    def __int__(self,_fileName=None):
        super(FileUtil, self).__int__(_fileName)

        pass


    def __del__(self):
        super(FileUtil, self).__del__()

        pass

    def ReadLine(self):
        return self.file.readline()
        pass

    pass

