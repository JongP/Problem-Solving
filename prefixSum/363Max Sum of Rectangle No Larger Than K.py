#hint from previous problem
from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m,n=len(matrix),len(matrix[0])
        prefixSum=self.getPrefixSum(matrix)
        res=-math.inf
        
        
        
        for i in range(m-1,-1,-1):
            for ii in range(i,-1,-1):
                arry=SortedList([0])
                total=0
                for j in range(n):
                    cur=prefixSum[ii][j]-prefixSum[i+1][j]
                    
                    total+=cur
                    idx=arry.bisect_left(total-k)#have to study
                    if idx<len(arry) and res<total-arry[idx]:
                        res=total-arry[idx]
                    
                    arry.add(total)
                    
        
        
        return res
        
        
    def getPrefixSum(self,matrix):
        m,n=len(matrix),len(matrix[0])
        res=[[0]*n for _ in range(m+1)]
        
        
        for i in range(m-1,-1,-1):
            for j in range(n):
                res[i][j]=res[i+1][j]+matrix[i][j]
        
        
        return res

#https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/1312722/Python-Two-solutions-explained
from sortedcontainers import SortedList
    
class Solution:
    def maxSumSubmatrix(self, M, k):
        def countRangeSum(nums, U):
            SList, ans = SortedList([0]), -float("inf")
            for s in accumulate(nums):
                idx = SList.bisect_left(s - U) 
                if idx < len(SList): ans = max(ans, s - SList[idx])        
                SList.add(s)
            return ans
        
        m, n, ans = len(M), len(M[0]), -float("inf")
        
        for i, j in product(range(1, m), range(n)):
            M[i][j] += M[i-1][j]
                
        M = [[0]*n] + M
        
        for r1, r2 in combinations(range(m + 1), 2):
            row = [j - i for i, j in zip(M[r1], M[r2])]
            ans = max(ans, countRangeSum(row, k))
            
        return ans
    