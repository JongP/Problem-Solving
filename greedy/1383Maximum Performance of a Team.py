from heapq import heappush,heappop

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        
        MOD=10**9+7
        heap=[]
        total=0
        
        engineers=sorted( [(e,s)   for e,s in zip(efficiency,speed)], reverse=True)
        
        res=0
        for e,s in engineers:
            if res<(total+s)*e:
                res = (total+s)*e
            
            heappush(heap,s)
            total+=s
            
            if len(heap)==k:
                total-=heappop(heap)
                
                
        return  res%MOD