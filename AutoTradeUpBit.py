import time
import datetime
from enum import Enum
import pyupbit

from FileWriter import FileWriter
from Log import Log, eLogType


class eIntervalType(Enum):
    DAY="day"
    MIN1 = "minute1"
    MIN3 = "minute3"
    MIN5 = "minute5"
    WEEK = "week"
    MONTH = "month"

class eTradeState(Enum):

    NONE = 0    # 어플이 시작됨 ..
    BUYING = 1  # 사서 들고 있음   --> 연속적으로  계속 sell 나와야 판다.....
    SELLING = 2 # 팔아 놓은 상태.............

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
                 _ticker , _tradeIntervalSec ,
                 _sellContinueCount ,
                 log=None):

        self.ticker = _ticker
        self.upbit = pyupbit.Upbit(_access, _secret)
        # 트레이드 간격
        self.tradeIntervalSec = _tradeIntervalSec
        # 판매시
        self.sellContinueCount = _sellContinueCount
        self.sellIngCount = 0
        self.tradeState = eTradeState.NONE

        self.fileWriter = None

        if log==None:
            self.log = Log("AutoTradeUpBit")
        else:
            self.log = log

        pass

    def __del__(self):
        if self.fileWriter != None:
            self.fileWriter.Close()

        pass

    def SetFileWriter(self,fileName):
        self.fileWriter = FileWriter(fileName)
        self.fileWriter.Open()
        pass

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

        while True:
            try:

                # now = datetime.datetime.now()

                ma15 = self.get_ma(eIntervalType.MIN1, 15)
                ma25 = self.get_ma(eIntervalType.MIN1, 25)
                ma50 = self.get_ma(eIntervalType.MIN1, 50)

                currentPrice = self.get_current_price()

                # print( " CP : " + str(currentPrice) + " ma15 : " + str(ma15) + " ma25 : " + str(ma25) + " ma50 : " + str(ma50))

                tPrice = []
                tPrice.append( TradePrice("cp" , currentPrice) )
                tPrice.append( TradePrice("ma15" , ma15) )
                tPrice.append( TradePrice("ma25" , ma25) )
                tPrice.append( TradePrice("ma50" , ma50) )

                tPrice.sort(key=lambda tradePrice : tradePrice.price , reverse=True )

                # sorted(tPrice , key=lambda tradePrice : tradePrice.price)

                loopCnt = 0
                for p in tPrice:
                    loopCnt +=1

                    self.log.Print( eLogType.INFO ,  f"""{loopCnt} {p.name} {p.price}""" )
                    # print( str(loopCnt) , " " , p.name , " " , str(p.price))
                # print(" ")
                self.log.Print( eLogType.INFO ,  " " )

                if currentPrice > ma15 and \
                    currentPrice > ma25 and \
                    currentPrice > ma50 :

                    self.sellIngCount = 0

                    if self.tradeState == eTradeState.NONE:
                        # print("Buy " , now , " Buy Price : " , str(currentPrice) )
                        self.buyTradePrice = TradePrice("Buy" , currentPrice)
                        # print("Buy " + self.buyTradePrice.ToString())
                        self.log.Print(eLogType.INFO, f"-Buy- {self.buyTradePrice.ToString()}")

                        self.FileWriteln( f"-Buy- {self.buyTradePrice.ToString()}" )

                        self.tradeState = eTradeState.BUYING
                else:
                    # print("sel")
                    if self.tradeState == eTradeState.BUYING:
                        self.sellIngCount+=1

                        self.log.Print(eLogType.INFO,
                                       f"""-Sell Try- {self.sellIngCount} {TradePrice("Sell", currentPrice).ToString()} Buying {self.buyTradePrice.ToString()}""")

                        self.FileWriteln(
                            f"""-Sell Try- cnt {self.sellIngCount} {TradePrice("Sell", currentPrice).ToString()} Buying {self.buyTradePrice.ToString()}""")

                        if self.sellIngCount > self.sellContinueCount:
                            # print("sell")

                            # print("Sell ", now, " Sell Price : ", str(currentPrice))
                            # print("Sell ", TradePrice("Sell" , currentPrice).ToString() , " Buying " , self.buyTradePrice.ToString())
                            self.log.Print(eLogType.INFO,f"""-Sell- {TradePrice("Sell" , currentPrice).ToString()} Buying {self.buyTradePrice.ToString()}""")

                            self.FileWriteln(f"""-Sell- {TradePrice("Sell" , currentPrice).ToString()} Buying {self.buyTradePrice.ToString()}""")

                            # 요때 마다 파일로 남길것 수익율 뭐 그런거....
                            self.sellIngCount = 0
                            self.tradeState = eTradeState.NONE

            except Exception as e:
                self.log.Print( eLogType.ERROR , e )
            finally:
                time.sleep(self.tradeIntervalSec)
            pass

        # f.close()

        pass



    pass


def main():

    # _access , _secret , _ticker , _tradeIntervalSec , _sellContinueCount

    log = Log("AutoTradeUpBit")

    autoTrade = AutoTradeUpBit("access" , "se" , "KRW-BTC" , 1 , 30,log)
    autoTrade.SetFileWriter("./tradeLog.txt")

    autoTrade.Run()

    pass

if __name__ == "__main__":
    main()