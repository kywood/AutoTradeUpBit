import os
from enum import Enum


class E_FILE_MODE(Enum):
    W="w"
    W_A="w+"
    R="r"
    RW="rw"
    A="a"
    A_A="a+"

    pass


class FileWriter:

    def __init__(self,_fileName=None):

        self.fileName = _fileName
        self.IsOpen = False
        self.file=None
        # self.fileCursor=None
        pass

    def __del__(self):
        self.Close()

        pass

    def Open(self,_fileMode=None):
        self.IsOpen=True

        if _fileMode == None:
            self.file = open(self.fileName, 'w+', newline="\n")
        else:
            self.file = open(self.fileName,_fileMode.value,newline="\n")

        return self

    #
    # def Open(self):
    #     self.IsOpen=True
    #     # self.file = open(self.fileName,'w',newline=os.linesep)
    #     self.file = open(self.fileName,'w',newline="\n")



    def Close(self):

        if self.IsOpen == True:
            self.file.close()

    def Write(self,message):
        if self.IsOpen != True:
            return

        self.file.writelines(message)
        self.file.flush()

    def Writeln(self,message):
        if self.IsOpen != True:
            return
        self.file.writelines(f"""{message}\n""")
        self.file.flush()

    pass


