import re
import sys
import threading
import platform

from AutoTradeUpBit import eTradeState, MAEle, eMAType, eIntervalType, TradePrice, AutoTradeUpBit
from DBMGR.IDB_Lists import IDB_Lists
from DBMGR.cDBManager import cDBManager
from DBMGR.cDBProperty import cMysqlProperty
from DBMGR.cDB_DEFINES import I_DB__ALIAS

from DBMGR.cMysqlDBOBJ import cMysqlDBOBJ
from Defines import E_RUN_MODE
from Log import Log, eLogType
from UpBitDataCollect import eCSVHeader
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

        fileCursor=FileUtil(self.DataFilePath).OpenCursor()

        DBObj = self.DBM.GetDbObject(E_DB_AS.MY_AUTO_TRADE)
        DBObj.Connect()

        qry = """insert into tradedata (`EVENT_TIME`, CURRENT_PRICE ,`MA8`, `MA15`, `MA25`, `MA50`)
        values(STR_TO_DATE('{0}','%Y%m%d%H%i%S'),{1},{2},{3},{4},{5})"""

        while fileCursor.Next():
            rs=re.sub("\r\n" , "" ,fileCursor.GetRecordSet())
            if rs.find(eCSVHeader.DATE_TIME.name) != -1:
                continue

            rss=rs.split(',')
            DBObj.GetUpdateQueue().AppendUpdateQry(qry.format(rss[0],rss[1],rss[2],rss[3],rss[4],rss[5]))

        DBObj.GetUpdateQueue().ExecuteUpdateAll()

    pass


class E_ARGV:
    SELF=0
    DATA_FILE=1
    RUN_MODE = 2
    MAX=3
    pass

def Usage(argv):
    print(f""" python ./app CsvFileName [runMode (0:debug 1:release)] """)
    pass

def main(argv):
    G_VERSION = "V.20220405-1"

    LoggingConfFile = "logging.conf"
    DataFile = "UpBitCollect.csv"

    if len(argv) == E_ARGV.MAX:
        RunMode = argv[E_ARGV.RUN_MODE]
        DataFile = argv[E_ARGV.DATA_FILE]
        return
    elif len(argv) == E_ARGV.MAX - 1:
        RunMode = E_RUN_MODE.DEBUG
        DataFile = argv[E_ARGV.DATA_FILE]
    else:
        Usage(argv)
        pass


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
    main(sys.argv)