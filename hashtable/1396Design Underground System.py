from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        #hashMap={Leyton: {Paradise: {startSum,endSum}}}
        self.hashMap=defaultdict(dict)
        self.people={}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.people[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start,sTime=self.people[id]
        
        if stationName not in self.hashMap[start]:
            self.hashMap[start][stationName] =[0,0]
        
        self.hashMap[start][stationName][0]+= t-sTime
        self.hashMap[start][stationName][1]+= 1
        
        del self.people[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        h=self.hashMap[startStation][endStation]
        
        return h[0]/h[1]
