# from D_Exception import D_AlreadyConnectException
import cx_Oracle

# from DBMGR import cDBOBJ
from DBMGR.cDBOBJ import cDBOBJ


class cOracleDBOBJ(cDBOBJ):
    def __init__(self , cDBProperty):
        cDBOBJ.__init__(self,cDBProperty)
        # self.mConn = None
        # self.mCursor = None
        # print "=============cOracleDBOBJ cDBProperty " , cDBProperty

    def Connect(self):
        if self.mConn != None:
            raise Exception("cOracleDBOBJ :: Connect  " , self.mConn )


        # self.mConn = cx_Oracle.connect( self.mProperty.ConnectInfo()  )
        self.mConn = cx_Oracle.connect( self.GetProperty().ConnectInfo())

        print("DLIB >> cOracleDBOCJ..Connect" , self.mConn)

        self.mCursor = self.mConn.cursor()





