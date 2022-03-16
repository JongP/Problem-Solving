from heapq import heappush,heappop
class Solution:
    #bucket sort, counting sort
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n=len(workers)
        res=[-1]*n
        cnt=0
        takenBike=set()
        
        
        heap=self.getDists(workers,bikes)
        
        for i in range(2000):
            while heap[i]:
                w,b =heappop(heap[i])
                if b not in takenBike and res[w]==-1:
                    res[w]=b
                    takenBike.add(b)
                    cnt+=1
            if cnt==n:
                break
        
        
        return res
        
        
    
    def getDists(self,workers,bikes):
        heap=collections.defaultdict(list)
        
        def getManDist(x1,y1,x2,y2):
            return abs(x1-x2)+abs(y1-y2)
        
        for i, (wx,wy) in enumerate(workers):
            for j, (bx,by) in enumerate(bikes):
                heappush(heap[getManDist(wx,wy,bx,by)],(i,j))
        
        return heap


#https://leetcode.com/problems/campus-bikes/discuss/308738/C%2B%2B-bucket-sort-O(M*N)-time-and-space-solution
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = [[] for i in range(2001)]
        for i, (x, y) in enumerate(workers):
            for j, (x_b, y_b) in enumerate(bikes):
                distance = abs(x - x_b) + abs(y - y_b)
                distances[distance].append((i, j))
        used_bikes = set()
        assignments = [-1] * len(workers)
        for distance in distances:
            for worker, bike in distance:
                if assignments[worker] == -1 and bike not in used_bikes:
                    used_bikes.add(bike)
                    assignments[worker] = bike
        return assignments