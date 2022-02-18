from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.smallHeap=[]
        self.largeHeap=[]

    def addNum(self, num: int) -> None:
        if self.largeHeap and num<self.largeHeap[0]:
            heappush(self.smallHeap,-1*num)
        else:
            heappush(self.largeHeap,num)
        
        if len(self.smallHeap)>len(self.largeHeap):
            heappush(self.largeHeap,-1*heappop(self.smallHeap))
        elif len(self.largeHeap)>len(self.smallHeap)+1:
            heappush(self.smallHeap,-1*heappop(self.largeHeap))

    def findMedian(self) -> float:
        if len(self.smallHeap)==len(self.largeHeap):
            return (self.largeHeap[0]-self.smallHeap[0])/2
        else:
            return self.largeHeap[0]



from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0