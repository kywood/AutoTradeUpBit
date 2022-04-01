import time
import datetime

import pyupbit

from LimitedList import LimitedList
from Log import Log, eLogType


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    li = LimitedList(3)

    li.Append("A")
    li.Append("B")
    li.Append("C")

    for dt in li.GetLists():
        print(dt)

    li.Append("1")
    li.Append("2")
    li.Append("3")
    li.Append("4")

    for dt in li.GetLists():
        print(dt)

    top = li.GetTop()
    bottom = li.GetBottom()

    print(top)
    print(bottom)

    #
    # log = Log()
    #
    # log.Print(eLogType.INFO , "test")
    #
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
