
# from cDB_DEFINES import *
from DBMGR.cDB_DEFINES import E_DB


class cDBProperty(object):
    #mDB_Type = None

    def __init__(self , db_type ):
        self.mDB_Type = db_type

    def ConnectInfo(self):
        print("cDBProperty::ConnectInfo")
        return None

    def GetDBType(self):
        return self.mDB_Type


    def GetArgs(self):
        return None

    def GetKwargs(self):
        return None


class cMysqlProperty(cDBProperty):

    # mAR=None
    # mKW=None


    def __init__(self , *args , **kwargs ):
        cDBProperty.__init__(self, E_DB.MYSQL)
        self.mArgs = args
        self.mKwargs = kwargs

    #
    # def __init__(self , id, pw, db_name , host_ip, port = 3306 ,  charset='utf8', use_unicode=True ):
    #     cDBProperty.__init__(self,E_DB.MYSQL  )
    #     #print "---------------------------------cMysqlProperty :: init"
    #     self.mHost_ip = host_ip
    #     self.mId = id
    #     self.mPw = pw
    #     self.mDB_NAME = db_name
    #     self.mCharset = charset
    #     self.mUse_unicode = use_unicode
    #     self.mPort = port


    def GetArgs(self):
        return self.mArgs

    def GetKwargs(self):
        return self.mKwargs


    def ConnectInfo(self):
        print("cMysqlProperty::ConnectInfo mDB_Type " , self.GetDBType())

        return self.mArgs, self.mKwargs
        # return self.mAR , self.mKW

        # return { 'host' : self.mHost_ip ,
        #          'user' :  self.mId ,
        #          'passwd' : self.mPw ,
        #          'db' : self.mDB_NAME }
        #
        # return { 'host' : self.mHost_ip ,
        #          'user' :  self.mId ,
        #          'password' : self.mPw ,
        #          'database' : self.mDB_NAME ,
        #         'charset' : self.mCharset ,
        #          'use_unicode' : self.mUse_unicode }

        #
        # return cMysqlProperty.mHost_ip,\
        #        cMysqlProperty.mId,\
        #        cMysqlProperty.mPw,\
        #        cMysqlProperty.mDB_NAME,\
        #        cMysqlProperty.mCharset,\
        #        cMysqlProperty.mUse_unicode,\
        #        cMysqlProperty.mPort


class cOracleProperty(cDBProperty):

    # tnsinfo ex) "id\passwd@db"
    def __init__(self , tns_info ):
        cDBProperty.__init__(self,E_DB.ORACLE )
        #print "---------------------------cOracleProperty :: init"
        self.mTnsInfo = tns_info

    def ConnectInfo(self):
        # print "cOracleProperty::ConnectInfo mDB_Type " , cDBProperty.mDB_Type
        return self.mTnsInfo


