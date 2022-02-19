#hint on related topic

from heapq import heappop,heappush
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append((target,0))
        heap=[]
        maxReach=startFuel
        res=0
        
        for pos, fuel in stations:
            #refuel
            while maxReach<pos and heap:
                maxReach-=heappop(heap)
                res+=1
            
            if maxReach<pos:
                return-1
            
            #take fuel
            heappush(heap,-fuel)
        
        return res



#https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/149839/DP-O(N2)-and-Priority-Queue-O(NlogN)
#dp[t] means the furthest distance that we can get with t times of refueling.
#dp[t + 1] = max(dp[t + 1], dp[t] + s[i][1])
#dp sol
    def minRefuelStops(self, target, startFuel, s):
        dp = [startFuel] + [0] * len(s)
        for i in range(len(s)):
            for t in range(i + 1)[::-1]:
                if dp[t] >= s[i][0]:
                    dp[t + 1] = max(dp[t + 1], dp[t] + s[i][1])
        for t, d in enumerate(dp):
            if d >= target: return t
        return -1


#greedy heap
    def minRefuelStops(self, target, cur, s):
        pq = []
        res = i = 0
        while cur < target:
            while i < len(s) and s[i][0] <= cur:
                heapq.heappush(pq, -s[i][1])
                i += 1
            if not pq: return -1
            cur += -heapq.heappop(pq)
            res += 1
        return res