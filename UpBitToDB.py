import re
import threading
import platform

from AutoTradeUpBit import eTradeState, MAEle, eMAType, eIntervalType, TradePrice, AutoTradeUpBit
from DBMGR.IDB_Lists import IDB_Lists
from DBMGR.cDBManager import cDBManager
from DBMGR.cDBProperty import cMysqlProperty
from DBMGR.cDB_DEFINES import I_DB__ALIAS

from DBMGR.cMysqlDBOBJ import cMysqlDBOBJ
from Log import Log, eLogType
from Utils.FileUtil import FileUtil
from Utils.FileWriter import E_FILE_MODE

global G_VERSION



class E_DB_AS(I_DB__ALIAS):
    MY_AUTO_TRADE = 100




class cDB_Info_Test( IDB_Lists ):
    def __init__(self):
        IDB_Lists.__init__(self ,
                           {
                               E_DB_AS.MY_AUTO_TRADE: cMysqlDBOBJ(
                                   cMysqlProperty(host='127.0.0.1', port=3306, user='AutoTrade', passwd='oracle', db='AutoTrade'))
                           })

class UpBitToDB :
    
    def __init__(self,_dbM, _dataFilePath , _log=None ):

        self.DBM = _dbM
        self.DataFilePath = _dataFilePath

        if _log==None:
            self.log = Log("UpBitDataCollect")
        else:
            self.log = _log

        pass

    def Run(self):

        file= FileUtil("UpBitCollect.csv").Open(E_FILE_MODE.R)

        DBObj = self.DBM.GetDbObject(E_DB_AS.MY_AUTO_TRADE)
        DBObj.Connect()

        param=[]
        qry="insert into MANY_TEST ( MA8 , MA15 ) values(%s,%s)"


        commitCnt = 50
        loopCnt=0

        while True:
            line = re.sub("\r\n" , "" , file.ReadLine() )

            if line == '':
                break
            else:
                print(line)
                param.append(["1","1"])
                DBObj.ExecBulkInsert( qry , param )
#                 DBObj.ExecuteUpdate( f"""
# insert into tradedata (`EVENT_TIME`, CURRENT_PRICE ,`MA8`, `MA15`, `MA25`, `MA50`)
# values(STR_TO_DATE('20220408150846','%Y%m%d%H%i%S'),54232000.0,54224000.0,54221733.333333336,54216160.0,54180680.0);
#                 """ )

            if loopCnt % commitCnt == 0:
                DBObj.Commit()

            loopCnt = loopCnt + 1

        DBObj.Commit()

    pass


def main():
    G_VERSION = "V.20220405-1"

    LoggingConfFile = "logging.conf"
    DataFile = "UpBitCollect.csv"

    basePath = "/home/oracle/Project/AutoTrade"

    if platform.system() == "Linux":
        LoggingConfFile = basePath + "/" + LoggingConfFile
        DataFile = basePath + "/" + DataFile

    log = Log("AutoTradeUpBit",_configFile=LoggingConfFile, _version=G_VERSION)

    DBM = cDBManager(cDB_Info_Test())
    dCollect = UpBitToDB( DBM , DataFile , log )
    dCollect.Run()

    pass

if __name__ == "__main__":
    main()