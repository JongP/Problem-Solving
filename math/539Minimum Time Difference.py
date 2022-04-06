class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def timeToMin(time):
            time=list(map(int,time.split(":")))
            return time[0]*60+time[1]
        
        mins=[]
        
        for time in timePoints:
            minute=timeToMin(time)
            mins.append(minute)
        
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def timeToMin(time):
            time=list(map(int,time.split(":")))
            return time[0]*60+time[1]
        
        mins=[]
        
        for time in timePoints:
            minute=timeToMin(time)
            mins.append(minute)
        

        mins.sort()
        mins.append(mins[0]+24*60)
        
        res=math.inf
        
        for i in range(1,len(mins)):
            if res>mins[i]-mins[i-1]:
                res=mins[i]-mins[i-1]
                
        return res

#https://leetcode.com/problems/minimum-time-difference/discuss/100637/Python-Straightforward-with-Explanation
def findMinDifference(self, A):
    def convert(time):
        return int(time[:2]) * 60 + int(time[3:])
    minutes = map(convert, A)
    minutes.sort()
    
    return min( (y - x) % (24 * 60) 
                for x, y in zip(minutes, minutes[1:] + minutes[:1]) )