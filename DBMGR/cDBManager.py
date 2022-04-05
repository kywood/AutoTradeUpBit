
# from DLIB_DEF import *
#from DLIB_DEF import DL_DEF

#
# class SingletonType(type):
#     def __call__(cls, *args, **kwargs):
#         try:
#             return cls.__instance
#         except AttributeError:
#             cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
#             return cls.__instance


class cDBManager(object):
    # __metaclass__ = SingletonType

    # mDBListObject = None

    def __init__(self , IDB_Lists ):
        # self.lock = Lock()

        self.__SetDBInfo( IDB_Lists )

        print ("cDBManager Initialize")

        # self.mDBListObject = None
        #log.setLoggerClass( cDBManager )

    # def Initialize(self):
    #     print "cDBManager Initialize"
        #log.info("cDBManager Initialize")

    def __del__(self):
        print("cDBManager Shutdown")
        self.CloseAll()


    def __SetDBInfo(self , IDB_Lists ):
        print("cDBManager::SetDBInfo")
        # with self.lock:
        self.mDBListObject = IDB_Lists
        # print "Cnt = ", len(self.mDBListObject.mDBInfoList)
        #
        # if DL_DEF.DEBUG == 1:
        #     print "Cnt = " , len(self.mDBListObject.mDBInfoList)
        #
        #     if len(self.mDBListObject.mDBInfoList) > 0 :
        #         for key , value in self.mDBListObject.mDBInfoList.iteritems():
        #             print "K-------------- : " , key , " V " , value
        #             print " V P " , value.mProperty
        #             print " V P TYPE  ", value.mProperty.mDB_Type

    def Connect(self , db_alias ):
        # print "cDBManager :: Connect " , db_alias
        self.GetDbObject( db_alias ).Connect()

    def Commit(self , db_alias):
        self.GetDbObject(db_alias).Commit()

    def Rollback(self , db_alias):
        self.GetDbObject(db_alias).RollBack()

    def ConnectAll(self):
        # print "cDBManager :: ConnectAll "
        for key,value in self.mDBListObject.mDBInfoList.items():
            self.Connect( key )
            # if DL_DEF.DEBUG == 1:
            #     print "K : ", key, " V ", value

    def CloseAll(self):
        for key,value in self.mDBListObject.mDBInfoList.items():
            self.Close( key )

    def Close(self ,db_alias ):
        self.GetDbObject( db_alias).Close()

    def ExecuteQuery(self ,db_alias,  qry):
        return self.GetDbObject(db_alias).ExecuteQuery( qry )


    def ExecuteUpdate(self ,db_alias,  qry):
        return self.GetDbObject(db_alias).ExecuteUpdate( qry )

    def IsConnect(self , db_alias):
        return self.GetDbObject(db_alias).IsConnect()

    def GetDbObject(self,db_alias):
        # print "cDBManager :: GetDbObject dba " , db_alias
        # print "cDBManager :: GetDbObject dba11 ", cDBManager.mDBObjS.GetDBObject(db_alias)
        # print "cDBManager :: GetDbObject dba22 " , cDBManager.mDBObjS.GetDBObject( db_alias).mProperty
        # print "cDBManager :: GetDbObject dba33 ", cDBManager.mDBObjS.GetDBObject(db_alias).mProperty.mDB_Type
        return self.mDBListObject.GetDBObject( db_alias)


    # def Test_Print(self):
    #     print "new_group_alarm_id 100\n"

