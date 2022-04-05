import threading
import platform
from AutoTradeUpBit import eTradeState, MAEle, eMAType, eIntervalType, TradePrice, AutoTradeUpBit
from Log import Log, eLogType
from MA import MA, eTrendDir
from Utils.Utils import Utils
global G_VERSION


class UpBitDataCollect(AutoTradeUpBit) :

    def __init__(self, _ticker, _queueSize , _maEleDict , _tradeIntervalSec=1, _buyContinueCount=0,
                 _sellContinueCount=0, _access="", _secret="" ,_log=None):

        super().__init__(_access, _secret, _ticker, _tradeIntervalSec, _buyContinueCount, _sellContinueCount, _log)


        if _log==None:
            self.log = Log("UpBitDataCollect")
        else:
            self.log = _log

        self.QueueSize = _queueSize
        self.MaEle = _maEleDict


    def RunAct(self,tPrice,dateFormat):

        currentTimeString = Utils.CurrentTimeString(dateFormat)

        currentPrice = self.get_current_price()
        tPrice[eMAType.CP.value] = TradePrice(eMAType.CP.value, currentPrice)

        # Trade MA
        for maName, maObj in self.Malists.GetLists().items():
            tPrice[maName] = TradePrice(maName, maObj.TradeMA())
            pass

        loopCnt = 0
        for key, tradePrice in tPrice.items():
            if tradePrice.name == eMAType.CP.value:
                self.log.Print(eLogType.INFO, f"""{loopCnt + 1} {tradePrice.name} {tradePrice.price}""")
            else:
                self.log.Print(eLogType.INFO,
                               f"""{loopCnt + 1} {tradePrice.name} {tradePrice.price} {self.Malists.GetMa(tradePrice.name).GetTrendDir()}""")
            # self.log.Print( eLogType.INFO ,  f"""{loopCnt + 1} {p.name} {p.price}""" )
            loopCnt += 1

        threading.Timer(self.tradeIntervalSec, self.RunAct, [tPrice, dateFormat]).start()

    def Run(self):
        self.log.Print(eLogType.INFO, "Start Run!!")

        for maEleKey , maEle in self.MaEle.items():
            # self.Malists.CreateMa(eMAType.MA8.value, MA(self.ticker, eIntervalType.MIN1, 8, self.QueueSize))

            if maEle.isActive == False:
                continue

            ma = MA(self.ticker, eIntervalType.MIN1, maEle.min)
            # ma.TradeMA()
            self.Malists.CreateMa(eMAType(maEle.maType).value, ma)
            pass

        tPrice = {}
        dateFormat = """%Y%m%d-%H:%M:%S"""
        self.RunAct(tPrice,dateFormat)

        #
        #
        # while True:
        #     time.sleep(10)
        #     pass

        pass


    pass


def main():
    G_VERSION = "V.20220405-1"

    CollectCycle = 1
    Ticker = "KRW-BTC"
    LoggingConfFile = "logging.conf"
    DataWriteFile = "UpBitCollect.txt"
    QueueSize=10

    MaEle = {
        eMAType.MA8.name: MAEle(eMAType.MA8, 8, True),
        eMAType.MA15.name: MAEle(eMAType.MA15, 15, True),
        eMAType.MA25.name: MAEle(eMAType.MA25, 25, True),
        eMAType.MA50.name: MAEle(eMAType.MA50, 50, True)
    }

    basePath = "/home/ubuntu/project/py/AutoTradeUpbit"

    if platform.system() == "Linux":
        LoggingConfFile = basePath + "/" + LoggingConfFile
        DataWriteFile = basePath + "/" + DataWriteFile

    log = Log("AutoTradeUpBit",_configFile=LoggingConfFile, _version=G_VERSION)

    dCollect = UpBitDataCollect( Ticker ,QueueSize, MaEle,CollectCycle , _log=log)
    dCollect.SetFileWriter(DataWriteFile)

    dCollect.Run()

    pass

if __name__ == "__main__":
    main()