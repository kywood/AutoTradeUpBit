

class LimitedList:

    def __init__(self , _size):
        self.Init(_size)
        pass

    def Init(self,_limitSize):
        self.limitSize = _limitSize
        self.lists = []

    def Append(self,_data):
        listsSize = len(self.lists)

        if listsSize + 1 > self.limitSize :
            del self.lists[0]
        self.lists.append(_data)

    def Count(self):
        return len(self.lists)

    def Get(self,index):
        return self.lists[index]

    def GetLists(self):
        return  self.lists

    def IsFill(self):

        if len(self.lists) >= self.limitSize:
            return True
        return False


    def GetTop(self):
        return self.lists[0]

    def GetBottom(self):
        return self.lists[len(self.lists) - 1]

    pass