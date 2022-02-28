#unsolved
#https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344898/Python-very-short-dp-solution-explained

#https://www.youtube.com/watch?v=STEJHYc9rMw
class Solution:
    #O(m*n^2)
    def maxPoints(self, points: List[List[int]]) -> int:
        m,n=len(points), len(points[0])
        
        dp=[0]*n
        left=[0]*n
        right=[0]*n
        
        for i in range(m):
            
            for j in range(n):
                if j==0:
                    left[j]=dp[j]
                else:
                    left[j]=max(dp[j],left[j-1]-1)
            
            for j in range(n-1,-1,-1):
                if j==n-1:
                    right[j]=dp[j]
                else:
                    right[j]=max(dp[j],right[j+1]-1)
                    
            
            for j in range(n):
                dp[j]=max(left[j],right[j])+points[i][j]
            
            #print(dp)
        
        return max(dp)



