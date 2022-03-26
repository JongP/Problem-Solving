from heapq import heappop, heappush
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        #[[1,3],[2,0],[5,10],[6,-10]]
        
        #vals=[2,-2,5,-4  ]
        #heap = [(2,1)]
        
        heap=[]
        res=-math.inf
        for x,y in points:
            while heap and x-heap[0][1]>k:
                heappop(heap)   
            
            if heap:
                res=max(res,-heap[0][0]+x+y)
            
            heappush(heap,(-(y-x),x))
                
        return res
    
    