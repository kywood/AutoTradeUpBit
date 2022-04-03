import time
import datetime
import platform
import pyupbit


import traceback

from AutoTradeUpBit import eMAType, TradePrice
from LimitedList import LimitedList
from Log import Log, eLogType


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #
    # li = LimitedList(3)
    #
    # li.Append("A")
    # li.Append("B")
    # li.Append("C")
    #
    # for dt in li.GetLists():
    #     print(dt)
    #
    # li.Append("1")
    # li.Append("2")
    # li.Append("3")
    # li.Append("4")
    #
    # for dt in li.GetLists():
    #     print(dt)
    #
    # top = li.GetTop()
    # bottom = li.GetBottom()
    #
    # print(top)
    # print(bottom)

    tPrice = dict()

    tPrice[eMAType.CP.value] = TradePrice(eMAType.CP.value, 10)
    tPrice[eMAType.MA15.value] = TradePrice(eMAType.MA15.value, 20)
    tPrice[eMAType.MA25.value] = TradePrice(eMAType.MA25.value, 3)
    tPrice[eMAType.MA50.value] = TradePrice(eMAType.MA50.value, 70)


    tPrice = dict(sorted(tPrice.items(), key=lambda tradePrice: tradePrice[1].price, reverse=True))



    # //print( tPrice.k )

    for k,v in tPrice.items():

        print(tPrice[k].ToString())

        pass

    platform.system()

    #
    #
    # log = Log()
    #
    # log.Print(eLogType.INFO , "test")
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
