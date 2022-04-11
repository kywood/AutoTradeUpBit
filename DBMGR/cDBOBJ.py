
#from threading import Lock
import logging


class cDBOBJ(object):
    # mConn = None
    # mCursor = None
    # mProperty = None

    def __init__(self ,cDBProperty):
        self.mConn = None
        self.mCursor = None
        self.mProperty = cDBProperty

    def GetProperty(self):
        return self.mProperty

    def Connect(self):
        print("cDBOCJ..Connect")

    def IsConnect(self):
        if self.mConn != None:
            return True
        else:
            return False

    def Commit(self):
        self.mConn.commit()

    def RollBack(self):
        self.mConn.rollback()

    def ExecuteMany(self,qry,param):
        self.mCursor.executemany(qry,param)
        pass

    def ExecuteQuery(self,qry):

        # print "ExecuteQuery ===== > " , self.mConn
        #return self.mConn.execute(qry).fetchall()
        # curr =  self.mConn.cursor().execute(qry)
        # return curr.fetchall()
        # return self.mConn.cursor().execute(qry).fetchall()
        self.mCursor.execute(qry)
        return self.mCursor.fetchall()


    def ExecuteUpdate(self,qry):
        # self.mCursor.execute(qry)
        try:
            self.mCursor.execute(qry)
        except Exception as ex:
            # print ("error ExecuteUpdate" , str(ex) , qry )
            logging.error("[Exception] ExecuteUpdate > "  + str(ex) + qry)
            raise  ex

    #
    # qry="insert into MANY_TEST ( MA8 , MA15 ) values(%s,%s)"
    # param=[]
    # param.append(["1","1"])
    # param.append(["2","2"])
    # param.append(["3","3"])
    # param.append(["4","4"])
    # param.append(["5","5"])
    # for arg in param:
    #     print(arg)
    #
    # DBObj.ExecBulkInsert( qry , param )
    # DBObj.Commit()

    def ExecBulkInsert(self , qry, data_list):
        self.mCursor.executemany( qry , data_list )


    def Close(self):

        if self.mConn == None:
            return

        self.mCursor.close()
        self.mConn.close()
        self.mConn = None




