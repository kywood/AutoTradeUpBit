#!/bin/env python
#-*-coding:cp949-*-
# from DBMGR import cDBOBJ
from DBMGR.cDBOBJ import cDBOBJ

try:
    import MySQLdb as mysql
except ImportError:
    import pymysql as mysql


class cMysqlDBOBJ(cDBOBJ):
    def __init__(self , cDBProperty):
        cDBOBJ.__init__(self,cDBProperty)

    def Connect(self):
        if self.mConn != None:
            raise Exception("cMysqlDBOBJ :: Connect  " , self.mConn)

        print("DLIB >> cMysqlDBOCJ..Connect " , self.GetProperty().ConnectInfo())
        #self.mConn = mysql.connect( self.mProperty.ConnectInfo() )
        # VV=( host='127.0.0.1', port=3306 , user='min', passwd='oracle', db='min' )
        # self.mConn = mysql.connect(  VV  )
        # self.mConn = mysql.connect(  '127.0.0.1'  , 'min' , 'oracle' , 'min'   )
        # self.mConn = mysql.connect( host='127.0.0.1', port=3306 , user='min', passwd='oracle', db='min' )
        self.mConn = mysql.connect(*self.mProperty.GetArgs() , **self.mProperty.GetKwargs() )
        self.mCursor = self.mConn.cursor()




