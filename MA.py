import pyupbit
from enum import Enum
from LimitedList import LimitedList


class eTrendDir(Enum):
    NONE = -1
    UP = 0
    DOWN = 1
    pass

class MA:

    def __init__(self,_ticker,_intervalType , _minAvg , _queueSize):
        self.ticker = _ticker
        self.intervalType = _intervalType
        self.minAvg = _minAvg

        self.limitLists = LimitedList(_queueSize)

        pass

    def TradeMA(self):
        df = pyupbit.get_ohlcv(self.ticker, interval=self.intervalType.value, count=self.minAvg)
        ma = df['close'].rolling(self.minAvg).mean().iloc[-1]
        self.limitLists.Append(ma)
        return ma

    def GetLastMA(self):
        return self.limitLists.GetLast()
        pass


    def GetTrendDir(self):

        if self.limitLists.IsFill() == False:
            return eTrendDir.NONE

        top = self.limitLists.GetFirst()
        bottom = self.limitLists.GetLast()

        if top < bottom:
            return eTrendDir.UP

        return eTrendDir.DOWN

        pass



    pass