#misunderstood the problem

#solved blinded
#could make big picture, but still can't come up with details and speical cases on my own.
from heapq import heappop, heappush
from collections import deque

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def getOffschedule(self,schedule):
        res=[]
        
        for s in schedule:
            tmpL=deque([])
            tmpL.append([-1*math.inf,s[0].start])
            for i in range(len(s)-1):
                tmpL.append([s[i].end,s[i+1].start])
            tmpL.append([s[-1].end,math.inf])
            res.append(tmpL)
        
        
        return res
    
    
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        offSchedule=self.getOffschedule(schedule)
        
        eHeap=[]
        sHeap=[]
        res=[]
        cnt=0
        
        for i,s in enumerate(offSchedule):
            heappush(sHeap,(s[0][0],i))
        
        while sHeap:
            curTime,curIdx=heappop(sHeap)
            
            while eHeap and eHeap[0][0]<curTime:
                eTime,eIdx=heappop(eHeap)
            
        
            s,e=offSchedule[curIdx].popleft()
            heappush(eHeap,(e,curIdx))
            if len(eHeap)>cnt:
                res.clear()
                cnt=len(eHeap)
            if eHeap and len(eHeap)==cnt and curTime!=-1*math.inf and curTime!=eHeap[0][0]:
                res.append(Interval(curTime,eHeap[0][0]))
            
            if offSchedule[curIdx]:
                heappush(sHeap,(offSchedule[curIdx][0][0],curIdx))
            

        if res[-1].end==math.inf:
            res.pop()
        
        return res
#nlog(n)
#merge intervals
#https://leetcode.com/problems/employee-free-time/discuss/767485/Easy-Python-Beats-95-with-Comments-and-Explanation!
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
		# Flatten the given intervals.
        ints = []
        for i in schedule:
            [ints.append(x) for x in i]
        
		# Sort the intervals by starting time which is a key part of this soln. and indentifying overlap.
        ints.sort(key = lambda x:x.start)
        
		# Now we want to merge intervals (the continuous periods of being busy).
        merged = []
        for i in ints:
		    # If we have no intervals in our list or the current task starts after the previous one ends.
            if not merged or i.start > merged[-1].end:
                merged.append(i)
            else:
			    # We know that the start time intersects the start,end of the previous task, so we take the max ending time.
				# As this will be a merged, continuous busy period.
                merged[-1].end = max(i.end, merged[-1].end)

        # Now we have our merged intervals we can look at the time between the merged 
		# intervals as these will be the free time for the employee. 
        free = []
        for i in range(1, len(merged)):
            free.append(Interval(start=merged[i-1].end, end=merged[i].start))
			
		# Now we're left with intervals of free time.
        return free

#nlogk
#merge k sorted interval
#https://leetcode.com/problems/employee-free-time/discuss/392763/easy-peasy-python-O(Nlog(K))-solution-where-K-is-of-employees
def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
    result = []
    heap = [ (emp[0].start, idx, 0) for idx, emp in enumerate(schedule) ]
    heapq.heapify(heap)
    
    # either take end or the start of the starting interval
    # minStart = schedule[heap[0][1]][0].end
    minStart = heap[0][0]
    
    while heap:
        t, e_id, colIdx = heapq.heappop(heap)
        
        if minStart < t:
            result.append(Interval(minStart, t))
            
        minStart = max(minStart, schedule[e_id][colIdx].end)
        
        if colIdx + 1 < len(schedule[e_id]):
            colIdx += 1
            heapq.heappush(heap, (schedule[e_id][colIdx].start, e_id, colIdx))
    
    return result
