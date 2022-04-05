

class IDB_Lists:

    # mDBList = {}
    # mDBInfoList = {}
    def __init__(self , db_info_list ):
        # int , cDBOBJ

        self.mDBInfoList={}

        self.mDBInfoList = db_info_list

        #print "IDB_L#ists init"

    def GetDBObject(self , db_alias):
        return self.mDBInfoList[db_alias]






