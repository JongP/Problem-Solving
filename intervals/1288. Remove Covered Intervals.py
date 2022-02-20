from heapq import heappop, heappush
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: (x[0],-x[1])) #hard coding for [[1,2],[1,4],[3,4]]
        heap=[]
        maxH=float('-inf')
        res=0
        
        for l,r in intervals:
            while heap and heap[0][0]<=l:
                heappop(heap)
                res+=1
                if not heap: maxH=float('-inf')
                
            if heap and r<=maxH:
                continue
                
            heappush(heap,(r,l))
            maxH=max(maxH,r)
            
        
        
        return res+len(heap)

# Idea

# Sort intervals by increasing of startTime and decreasing of endTime
# last = -1: last is the farest end time of browsed intervals
# For each interval in intervals
# If interval.endTime <= last, means interval is overlapped then we count removed
# else last = interval.endTime
# Result = number of intervals - removed
#https://leetcode.com/problems/remove-covered-intervals/discuss/878251/JavaPython-Sorting-Clean-and-Concise-O(NlogN)
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key = lambda x:(x[0], -x[1]))
        last = -1
        removed = 0
        for i in intervals:
            if i[1] <= last:
                removed += 1
            else:
                last = i[1]
        return len(intervals) - removed

#https://leetcode.com/problems/remove-covered-intervals/solution/
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start point.
        # If two intervals share the same start point
        # put the longer one to be the first.
        intervals.sort(key = lambda x: (x[0], -x[1]))
        count = 0
        
        prev_end = 0
        for _, end in intervals:
            # if current interval is not covered
            # by the previous one
            if end > prev_end:
                count += 1    
                prev_end = end
        
        return count