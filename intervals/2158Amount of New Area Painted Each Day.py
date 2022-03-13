#hint on line 19 for loop
from heapq import heappop,heappush
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:

        heap=[]
        res=[0]*len(paint)
        ended=set()
        
        points=[]
        for i,(x,y) in enumerate(paint):
            points.append((x,i,True))    
            points.append((y,i,False))
        points.sort()
        
        
        
        i=0
        for pos in range(points[-1][0]+1):#key point
            
            while i<len(points) and points[i][0]==pos:
                _,idx,isStart=points[i]
                
                if isStart:
                    heappush(heap,idx)
                else:
                    ended.add(idx)
                i+=1
                
            while heap and heap[0] in ended:
                heappop(heap)
            
            if heap:
                res[heap[0]]+=1
            
        return res


#RB tree -- sortedcontainers, SortedList
#https://leetcode.com/problems/amount-of-new-area-painted-each-day/discuss/1740812/Python-Complete-3-solutions-using-different-data-structures
from sortedcontainers import SortedList
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        # constructure the sweep line
        records = []
        max_pos = 0
        for i, [start, end] in enumerate(paint):
            records.append((start, i, 1)) # use 1 and -1 to records the type.
            records.append((end, i, -1))
            max_pos = max(max_pos, end)
        records.sort()

        # sweep across all position
        ans = [0 for _ in range(len(paint))]
        indexes = SortedList()
        i = 0
        for pos in range(max_pos + 1):
            while i < len(records) and records[i][0] == pos:
                pos, index, type = records[i]
                if type == 1:
                    indexes.add(index)
                else:
                    indexes.remove(index)
                i += 1
            if indexes:
                ans[indexes[0]] += 1
        return ans