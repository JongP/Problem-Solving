from heapq import heappush,heappop
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        2,3,5
        (i,j,k)  non-negative integer
        
        1,2,3,2^2,5
        2*3,2^3,3^2,2*5,2^2*3,3*5
        
        0,0,0
        1 0 0
        0 1 0
        2 0 0
        0 0 1
        1 1 0
        3 0 0
        
        heap = [1]
        
        heappop(1)
        1 (2,3,5)
        
        """
        visited=set([1])
        heap=[1]
        
        
        for _ in range(n):
            cur=heappop(heap)
            
            for mul in [2,3,5]:
                if cur*mul not in visited:
                    visited.add(cur*mul)
                    heappush(heap,cur*mul)
            
            
        return cur

#https://leetcode.com/problems/ugly-number-ii/discuss/718879/Python-O(n)-universal-dp-solution-explained
class Solution:
    def nthUglyNumber(self, n):
        factors, k = [2,3,5], 3
        starts, Numbers = [0] * k, [1]
        for i in range(n-1):
            candidates = [factors[i]*Numbers[starts[i]] for i in range(k)]
            new_num = min(candidates)
            Numbers.append(new_num)
            starts = [starts[i] + (candidates[i] == new_num) for i in range(k)]
        return Numbers[-1]