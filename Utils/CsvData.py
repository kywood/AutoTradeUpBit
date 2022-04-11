

class CsvData:

    def __init__(self,_rowData=None):
        self.rows=[]

        if _rowData != None:
            self.rows=_rowData
        pass

    def Append(self,_dt):
        self.rows.append(_dt)
        return self
        pass

    def Appends(self,_rowData):
        self.rows.append(_rowData)
        return self

    def GetRows(self):
        return self.rows
