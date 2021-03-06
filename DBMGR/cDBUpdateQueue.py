

class cDBUpdateQueue(object):

    def __init__(self,_dbObj,_commitCycle=50):

        self.DBObj=_dbObj
        self.UpdateQueue=[]
        self.CommitCycle=_commitCycle
        self.CommitCnt=0

        pass
    def SetCommitCycle(self,_commitCycle):
        self.CommitCycle = _commitCycle
        pass

    def AppendQry(self,_updateQry):
        self.UpdateQueue.append(_updateQry)
        self.CommitCnt = self.CommitCnt+1

        if self.CommitCnt >= self.CommitCycle:
            self.ExecuteAll()


    def ExecuteAll(self):
        if len(self.UpdateQueue) <= 0:
            return

        for update_qry in self.UpdateQueue:
            self.DBObj.ExecuteUpdate(update_qry)

        self.DBObj.Commit()
        self.CommitCnt=0

    pass