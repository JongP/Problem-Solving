class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        
        dp=[[-1]*n for _ in range(m)]
        dp[-1][-1]=grid[-1][-1]
        
        
        def helper(x,y):
            if x<0 or x>=m or y<0 or y>=n : return math.inf
            if dp[x][y]!=-1: return dp[x][y]
            
            res=grid[x][y]+min(helper(x+1,y),helper(x,y+1))
            
            dp[x][y]=res
            
            return dp[x][y]
        
        return helper(0,0)

#in-place
#https://leetcode.com/problems/minimum-path-sum/discuss/1467216/Python-Bottom-up-DP-In-place-Clean-and-Concise
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    pass
                elif r == 0:
                    grid[r][c] += grid[r][c-1]
                elif c == 0:
                    grid[r][c] += grid[r-1][c]
                else:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        return grid[m-1][n-1]