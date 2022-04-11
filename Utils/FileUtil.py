import os
import sys

from Utils.FileWriter import FileWriter, E_FILE_MODE


class FileCursor:

    def __init__(self,_fileUtil):
        self.FileUtil = _fileUtil
        self.file=None
        self.rs=None
        pass

    def OpenCurson(self):
        self.FileUtil.Open(E_FILE_MODE.R)
        self.file=self.FileUtil.file
        pass

    def GetRecordSet(self):
        return self.rs
        pass

    def Next(self):
        self.rs=self.file.readline()
        if self.rs=='':
            return False
        return True
    pass

class FileUtil(FileWriter):

    def __init__(self,_fileName=None):
        super().__init__(_fileName)
        # super(FileUtil, self).__int__(_fileName)
        self.fileCursor=FileCursor(self)
        pass

    def __del__(self):
        super().__del__()
        pass

    def OpenCursor(self):
        self.fileCursor.OpenCurson()
        return self.fileCursor

    def ReadLine(self):
        return self.file.readline()
        pass

    pass

