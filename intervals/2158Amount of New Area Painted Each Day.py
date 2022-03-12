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