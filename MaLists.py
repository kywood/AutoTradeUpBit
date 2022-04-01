

class MaLists:

    def __init__(self):
        self.Malists={}
        pass

    def CreateMa(self,_name,_ma):
        self.Malists[_name] =_ma
        pass


    def IsTrendDir(self,trendDir):
        for ma in self.Malists.values():
            if ma.GetTrendDir() != trendDir:
                return False

        return True

    def GetMa(self,_name):

        return self.Malists[_name]
        pass

    def Contains(self,_name):
        if _name in self.Malists:
            return True
        else:
            return False

    def GetLists(self):
        return self.Malists

    def Count(self):
        return len(self.Malists)

    pass