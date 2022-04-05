import os
import time
import datetime
import platform
import pyupbit


import traceback

from AutoTradeUpBit import eMAType, TradePrice
from LimitedList import LimitedList
from Log import Log, eLogType
from UpBitDataCollect import eCSVHeader
from Utils.Csv import CustomCsv
from Utils.CsvData import CsvData


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    log = Log(_version="v1")
    log.Print(eLogType.INFO , "test")


    csv=CustomCsv("./UpBitCollect.txt")
    csv.Open()

    # csvData = CsvData()
    # csvData.Append(1).Append("3")
    # # csvData.Append("3")
    # csvData.Append("korea")
    #
    # csvData2=CsvData([2,"100","usa"])
    #

    csv.WriteHead(eCSVHeader.GetRowdata())

    # csv.WriteRowData([1,"bb","cc"])
    # csv.WriteRowData([2,"bb","cc"])
    # csv.WriteRowData([4,"bb","cc"])
    # csv.WriteRowData([6,"bb","cc"])
    # csv.WriteRowData(csvData.GetRows())
    # csv.WriteRowData(csvData2.GetRows())


    csv.Close()



    #
    # a=10
    # b=100
    # c=1000
    #
    #
    # lili = LimitedList(3)
    #
    # lili.Append(10)
    # lili.Append(20)
    # lili.Append(30)
    #
    # print(lili)
    #
    # lili.Append(100)
    # lili.Append(200)
    #
    # print(lili)

#
#     print(f"""{eMAType.MA15.name} {eMAType.MA15.value} {eMAType.MA15}""")
#
#     log.Print(eLogType.INFO, f"""-sell-\n{a}\n{b}\n{c}""")
#     log.Print(eLogType.INFO, f"""-sell-
# {a}
# {b}
# {c}""")

    #
    # tPrice = dict()
    #
    # tPrice[eMAType.CP.value] = TradePrice(eMAType.CP.value, 10)
    # tPrice[eMAType.MA15.value] = TradePrice(eMAType.MA15.value, 20)
    # tPrice[eMAType.MA25.value] = TradePrice(eMAType.MA25.value, 3)
    # tPrice[eMAType.MA50.value] = TradePrice(eMAType.MA50.value, 70)
    #
    # tPrice = dict(sorted(tPrice.items(), key=lambda tradePrice: tradePrice[1].price, reverse=True))
    #
    # for k,v in tPrice.items():
    #     print(tPrice[k].ToString())
    #     pass
    #
    # platform.system()

    #
    #

    #
    # try:
    #
    #     a=[]
    #     a[10]=10
    #
    # except Exception as e:
    #
    #     log.Print(eLogType.ERROR,traceback.format_exc())
    #
    #     pass


    #
    # now = datetime.datetime.now().strftime("""%Y%m%d%H%M%S""")
    #
    # print(f"N:{str(now)}")
    #
    # f=open("./test2.txt" , 'a+')
    # f.writelines("tet1\n")
    # f.writelines("tet2\n")
    # f.writelines("tet3\n")
    # f.writelines("tet4\n")
    # f.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
