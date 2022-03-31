

class FileWriter:

    def __init__(self,_fileName=None):

        self.fileName = _fileName
        self.IsOpen = False
        pass

    def __del__(self):
        self.Close()

        pass

    def Open(self):
        self.IsOpen=True
        self.file = open(self.fileName,'a+')
        pass

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