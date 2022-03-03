from heapq import heappop,heappush
class StockPrice:

    def __init__(self):
        self.d={}
        self.maxHeap=[]
        self.minHeap=[]
        self.maxTime=0

    def update(self, timestamp: int, price: int) -> None:
        self.d[timestamp]=price
        
        if timestamp>self.maxTime:
            self.maxTime=timestamp
            
        heappush(self.maxHeap,(-price,timestamp))
        heappush(self.minHeap,(price,timestamp))
            

    def current(self) -> int:
        return self.d[self.maxTime]

    def maximum(self) -> int:
        while self.d[self.maxHeap[0][1]]!=-self.maxHeap[0][0]:
            heappop(self.maxHeap)
        
        return -self.maxHeap[0][0]

    def minimum(self) -> int:
        while self.d[self.minHeap[0][1]]!=self.minHeap[0][0]:
            heappop(self.minHeap)
        
        return self.minHeap[0][0]


#https://leetcode.com/problems/stock-price-fluctuation/discuss/1513413/JavaC%2B%2BPython-Strightforward-Solutions
#https://www.geeksforgeeks.org/python-sorted-containers-an-introduction/
from sortedcontainers import SortedDict

class StockPrice:

    def __init__(self):
        self.time_to_prices = SortedDict()
        self.rec = SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time_to_prices:
            prev_price = self.time_to_prices[timestamp]
            self.rec[prev_price].remove(timestamp)
            if len(self.rec[prev_price]) == 0:
                self.rec.pop(prev_price)
        if not price in self.rec:
            self.rec[price] = set()
        self.rec[price].add(timestamp)
        self.time_to_prices[timestamp] = price

    def current(self) -> int:
        return self.time_to_prices.peekitem(-1)[1]

    def maximum(self) -> int:
        return self.rec.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.rec.peekitem(0)[0]