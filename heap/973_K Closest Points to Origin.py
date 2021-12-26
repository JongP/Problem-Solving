import heapq
class Solution:
    #O(nlogk) O(k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        res=[]
        
        
        for i in range(k):
            heapq.heappush(heap,(-1*(points[i][0]**2+points[i][1]**2),i))
            
            
        for i in range(k,len(points)):
            mDSqr=-1*(points[i][0]**2+points[i][1]**2)
            if heap[0][0]<mDSqr:
                heapq.heappop(heap)
                heapq.heappush(heap,(mDSqr,i))
                
        
        while heap:
            idx=heapq.heappop(heap)[1]
            res.append(points[idx])
            
        return res


#https://leetcode.com/problems/k-closest-points-to-origin/discuss/217999/JavaC%2B%2BPython-O(N)
#nsmallest
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)
