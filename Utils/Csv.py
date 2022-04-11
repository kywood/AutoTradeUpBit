import csv

from Utils.FileWriter import FileWriter


class CustomCsv(FileWriter):

    def __init__(self,_fileName=None):
        super().__init__(_fileName)
        self.wr = None

    def Open(self):
        super().Open()
        self.wr = csv.writer(self.file)

    def WriteHead(self, rowData):
        self.__WriteRow(rowData)

    def WriteRowData(self,rowData):
        self.__WriteRow(rowData)

    def __WriteRow(self,rowData):
        self.wr.writerow(rowData)
        self.file.flush()
        # self.wr.flush
        pass

    pass