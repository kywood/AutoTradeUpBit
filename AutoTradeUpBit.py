import time
import datetime
from enum import Enum
import pyupbit
import platform

import traceback

from typing import Dict

from Utils.FileWriter import FileWriter
from Log import Log, eLogType
from MA import MA, eTrendDir
from MaLists import MaLists
from Utils.Utils import Utils

global G_VERSION




class MAEle:

    def __init__(self,_ematype , _min , _active=True):
        self.maType = _ematype
        self.min = _min
        self.isActive = _active
        pass

    pass

class eMAType(Enum):
    CP = "cp"
    MA8 = "ma8"
    MA15 = "ma15"
    MA25 = "ma25"
    MA50 = "ma50"



class eIntervalType(Enum):
    DAY="day"
    MIN1 = "minute1"
    MIN3 = "minute3"
    MIN5 = "minute5"
    WEEK = "week"
    MONTH = "month"

class eTradeState(Enum):

    NONE = 0    # 어플이 시작됨 ..
    READY = 1
    BUY_TRY = 2  # 살려고 노력중
    BUYING = 3  # 사서 들고 있음
    SELL_TRY = 4  # 팔려고 시도중
    SELLING = 5 # 팔아 놓은 상태.............

class TradePrice :

    def __init__(self , _name , _price):
        self.name = _name
        self.price = _price
        self.UpdateTime()

    def UpdateTime(self):
        self.time = datetime.datetime.now()

    def ToString(self):
        return "Name : " + self.name + " price : " + str(self.price) + " time : " + str(self.time)


class AutoTradeUpBit :

    def __init__(self,_access , _secret ,
                 _ticker , _queueSize , _tradeIntervalSec ,
                 _buyContinueCount ,
                 _sellContinueCount ,
                 log=None):

        self.ticker = _ticker
        self.upbit = pyupbit.Upbit(_access, _secret)
        # 트레이드 간격
        self.tradeIntervalSec = _tradeIntervalSec

        self.QueueSize = _queueSize
        self.buyContinueCount = _buyContinueCount
        # 판매시
        self.sellContinueCount = _sellContinueCount
        self.sellIngCount = 0
        self.tradeState = eTradeState.NONE

        self.fileWriter = None

        # self.QueueSize = 0;

        self.Malists = MaLists()

        if log==None:
            self.log = Log("AutoTradeUpBit")
        else:
            self.log = log

        self.MaEle = {
            eMAType.MA8.name :  MAEle( eMAType.MA8 ,8,True ) ,
            eMAType.MA15.name :  MAEle( eMAType.MA15 ,15,False) ,
            eMAType.MA25.name :  MAEle( eMAType.MA25 ,25,False) ,
            eMAType.MA50.name :  MAEle( eMAType.MA50 ,50,True)
        }

        pass

    def __del__(self):
        if self.fileWriter != None:
            self.fileWriter.Close()
        pass

    def GetMaEle(self,eMaType):
        return self.MaEle[eMaType.name]


    def SetFileWriter(self,fileName):
        self.fileWriter = FileWriter(fileName)
        self.fileWriter.Open()
        pass

    def SetMaQueueSize(self,queueSize):
        self.QueueSize=queueSize

    def FileWriteln(self,message):

        if self.fileWriter == None:
            return
        self.fileWriter.Writeln(message)

        pass


    def get_ma(self, intervalType , counts):
        """counts일 이동 평균선 조회"""
        df = pyupbit.get_ohlcv( self.ticker, interval=intervalType.value, count=counts)
        ma = df['close'].rolling(counts).mean().iloc[-1]
        return ma

    def get_current_price(self):
        """현재가 조회"""
        # return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]
        return pyupbit.get_current_price(self.ticker)

    def get_balance(self):
        """잔고 조회"""
        balances = self.upbit.get_balances()
        for b in balances:
            if b['currency'] == self.ticker:
                if b['balance'] is not None:
                    return float(b['balance'])
                else:
                    return 0
        return 0



    def Run(self):

        self.log.Print( eLogType.INFO ,"Start Run!!")

        # f = open("./test.txt", 'w')



        dateFormat = """%Y%m%d-%H:%M:%S"""

        # self.Malists.CreateMa( eMAType.MA8.value ,  MA( self.ticker , eIntervalType.MIN1 , 8 , self.QueueSize ) )
        # self.Malists.CreateMa( eMAType.MA15.value , MA( self.ticker , eIntervalType.MIN1 , 15 , self.QueueSize ) )
        # self.Malists.CreateMa( eMAType.MA25.value , MA( self.ticker , eIntervalType.MIN1 , 25 , self.QueueSize ) )
        # self.Malists.CreateMa( eMAType.MA50.value , MA( self.ticker , eIntervalType.MIN1 , 50 , self.QueueSize ) )

        for maEleKey , maEle in self.MaEle.items():
            # self.Malists.CreateMa(eMAType.MA8.value, MA(self.ticker, eIntervalType.MIN1, 8, self.QueueSize))

            if maEle.isActive == False:
                continue

            ma = MA(self.ticker, eIntervalType.MIN1, maEle.min, self.QueueSize)
            # ma.TradeMA()
            self.Malists.CreateMa(eMAType(maEle.maType).value, ma)
            pass

        while True:
            try:
                # ma8  = self.Malists.GetMa( eMAType.MA8.value ).TradeMA()
                # ma15 = self.Malists.GetMa( eMAType.MA15.value ).TradeMA()
                # ma25 = self.Malists.GetMa( eMAType.MA25.value ).TradeMA()
                # ma50 = self.Malists.GetMa( eMAType.MA50.value ).TradeMA()

                currentPrice = self.get_current_price()

                tPrice = {}
                tPrice[eMAType.CP.value]  =  TradePrice( eMAType.CP.value , currentPrice)

                # Trade MA
                for maName , maObj in self.Malists.GetLists().items() :
                    tPrice[maName] = TradePrice(maName, maObj.TradeMA() )
                    pass
                #
                # tPrice[eMAType.MA8.value] = TradePrice(eMAType.MA8.value , ma8)
                # tPrice[eMAType.MA15.value] = TradePrice(eMAType.MA15.value , ma15)
                # tPrice[eMAType.MA25.value] = TradePrice(eMAType.MA25.value , ma25)
                # tPrice[eMAType.MA50.value] = TradePrice(eMAType.MA50.value , ma50)

                # ma8  = self.Malists.GetMa( eMAType.MA8.value ).GetLastMA()
                # ma15 = self.Malists.GetMa( eMAType.MA15.value ).GetLastMA()
                # ma25 = self.Malists.GetMa( eMAType.MA25.value ).GetLastMA()
                # ma50 = self.Malists.GetMa( eMAType.MA50.value ).GetLastMA()

                tPrice = dict(sorted(  tPrice.items() , key= lambda tradePrice : tradePrice[1].price , reverse=True))

                currentTimeString = Utils.CurrentTimeString(dateFormat)

                loopCnt = 0
                for key , tradePrice  in tPrice.items():
                    if tradePrice.name == eMAType.CP.value:
                        self.log.Print(eLogType.INFO, f"""{loopCnt + 1} {tradePrice.name} {tradePrice.price}""")
                    else:
                        self.log.Print(eLogType.INFO,
                                       f"""{loopCnt + 1} {tradePrice.name} {tradePrice.price} {self.Malists.GetMa(tradePrice.name).GetTrendDir()}""")
                    # self.log.Print( eLogType.INFO ,  f"""{loopCnt + 1} {p.name} {p.price}""" )

                    loopCnt += 1
                self.log.Print( eLogType.INFO ,  " " )

                if self.Malists.IsTrendBreak(currentPrice) == True :
                # if currentPrice > ma8 and \
                #     currentPrice > ma15 and \
                #     currentPrice > ma25 and \
                #     currentPrice > ma50 :

                    self.sellIngCount = 0

                    if self.tradeState == eTradeState.NONE:
                        self.log.Print(eLogType.INFO, " = Current TradeState Locked = ")
                        pass
                    elif self.tradeState == eTradeState.READY:

                        self.buyTryCount = 0
                        self.tradeState = eTradeState.BUY_TRY


                    if self.tradeState == eTradeState.BUY_TRY:

                        isTrendDirUP = self.Malists.IsTrendDir(eTrendDir.UP)

                        self.log.Print(eLogType.INFO,
                                       f"-Buy try- {self.buyTryCount} ISTrendDirUP : {isTrendDirUP} price : {currentPrice} TIME:{ currentTimeString }")
                        self.FileWriteln(f"-Buy try- {self.buyTryCount} ISTrendDirUP : {isTrendDirUP} price : {currentPrice} TIME:{ currentTimeString }")

                        if isTrendDirUP == False:

                            self.tradeState = eTradeState.READY
                        else:
                            # 여기서 업이 아니면 다시 돌아간다...

                            self.buyTryCount += 1
                            if self.buyTryCount > self.buyContinueCount:

                                self.buyTradePrice = TradePrice("Buy", currentPrice)
                                self.log.Print(eLogType.INFO, f"-Buy- {self.buyTradePrice.ToString()}")
                                self.FileWriteln(f"-Buy- {self.buyTradePrice.ToString()}")
                                self.tradeState = eTradeState.BUYING
                else:

                    if self.tradeState == eTradeState.NONE:
                        self.log.Print(eLogType.INFO," == Trading Start ==")
                        self.tradeState = eTradeState.READY

                    if self.tradeState == eTradeState.BUYING:
                        self.sellIngCount+=1

                        SellTradePrice = TradePrice("Sell", currentPrice)

                        self.log.Print(eLogType.INFO,
                                       f"""-Sell Try- {self.sellIngCount} {SellTradePrice.ToString()} Buying {self.buyTradePrice.ToString()}""")

                        self.FileWriteln(
                            f"""-Sell Try- cnt {self.sellIngCount} {SellTradePrice.ToString()} Buying {self.buyTradePrice.ToString()}""")

                        if self.sellIngCount > self.sellContinueCount:
                            # print("sell")

                            # print("Sell ", now, " Sell Price : ", str(currentPrice))
                            # print("Sell ", TradePrice("Sell" , currentPrice).ToString() , " Buying " , self.buyTradePrice.ToString())
                            self.log.Print(eLogType.INFO,f"""-Sell-
{SellTradePrice.ToString()}
Buying {self.buyTradePrice.ToString()}
Result : {str(self.buyTradePrice.price - SellTradePrice.price)}
Avg : {str((self.buyTradePrice.price - SellTradePrice.price) / self.buyTradePrice * 100)}
""")

                            self.FileWriteln(f"""-Sell- 
{SellTradePrice.ToString()} 
Buying {self.buyTradePrice.ToString()}
Result : {str(self.buyTradePrice.price - SellTradePrice.price)}
Avg : {str((self.buyTradePrice.price - SellTradePrice.price) / self.buyTradePrice * 100)}
""")

                            # 요때 마다 파일로 남길것 수익율 뭐 그런거....
                            self.sellIngCount = 0
                            self.tradeState = eTradeState.READY

            except Exception as e:
                self.log.Print( eLogType.ERROR , traceback.format_exc() )
            finally:
                time.sleep(self.tradeIntervalSec)
            pass

        # f.close()
        pass

    pass


def main():
    G_VERSION = "V.20220403-1"

    buyTryCnt = 20
    sellTryCnt = 20
    ticker = "KRW-BTC"
    fileLoggingConf = "logging.conf"
    fileTradeLog = "tradeLog.txt"
    basePath = "/home/oracle/Project/AutoTrade"

    QueueSize=10

    if platform.system() == "Linux":
        fileLoggingConf = basePath + "/" + fileLoggingConf
        fileTradeLog = basePath + "/" + fileTradeLog

    log = Log("AutoTradeUpBit",_configFile=fileLoggingConf, _version=G_VERSION)

    autoTrade = AutoTradeUpBit("access" , "se" , ticker ,QueueSize, 1 , buyTryCnt,sellTryCnt,log)
    autoTrade.SetFileWriter(fileTradeLog)
    # autoTrade.SetMaQueueSize(10)

    # log.Print(eLogType.INFO,AppStart{})
    autoTrade.Run()

    pass

if __name__ == "__main__":
    main()