#nlog(n)
import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips=sorted(trips,key= lambda x: (x[1],x[2]))
        heap=[]
        #print(trips)
        cur=0
        for c,f,t in trips:
            while heap and heap[0][0]<=f:
                cur-=heapq.heappop(heap)[1]                
            cur+=c
            if cur>capacity:
                return False
            heapq.heappush(heap,(t,c))
            
            
        return True

#https://leetcode.com/problems/car-pooling/discuss/319088/Simple-Python-solution
 def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        lst.sort()
        pas = 0
        for loc in lst:
            pas += loc[1]
            if pas > capacity:
                return False
        return True