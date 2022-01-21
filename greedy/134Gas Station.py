#hint on related topic(greedy, O(n))
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #O(n), O(n)
        data=[g-c for g,c in zip(gas,cost)]
        
        if sum(data)<0: return -1
        
        res=-1
        total=0
        
        for i in range(len(data)):
            total+=data[i]
            if total<0:
                res=-1
                total=0
            elif res==-1:
                res=i
        
        
        
        return res



#https://leetcode.com/problems/gas-station/discuss/1706142/JavaC%2B%2BPython-An-explanation-that-ever-EXISTS-till-now!!!!
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start