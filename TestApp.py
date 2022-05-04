import os
import re
import time
import datetime
import platform
import pyupbit


import traceback

from AutoTradeUpBit import eMAType, TradePrice
from DBMGR.cDBManager import cDBManager
from LimitedList import LimitedList
from Log import Log, eLogType
from UpBitDataCollect import eCSVHeader
from UpBitToDB import cDB_Info_Test
from UpBitToDB import E_DB_AS
from Utils.Csv import CustomCsv
from Utils.CsvData import CsvData
from Utils.FileUtil import FileUtil


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    log = Log(_version="v1")
    log.Print(eLogType.INFO , "test")

    fileUtil = FileUtil("config.conf")

    f= FileUtil()

    cursor=fileUtil.OpenCursor()

    while cursor.Next():

        print( re.sub( "\r\n" , "" , cursor.rs) )

        pass


    # str="UpBitCollectSample.csv"
    # strL=str.split('.')
    #
    # print(strL)
    #
    # strS="".join(strL)
    #
    # print(strS)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
