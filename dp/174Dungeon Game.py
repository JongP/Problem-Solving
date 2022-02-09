class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n=len(dungeon),len(dungeon[0])
        
        dp=[[None]*n for _ in range(m)]
        dp[-1][-1]=max(1-dungeon[-1][-1],1)
        
        def helper(x,y):
            if dp[x][y]!=None: return dp[x][y]
            
            res=math.inf
            val=dungeon[x][y]
            
            if x<m-1:
                res=min(res,helper(x+1,y))
            if y<n-1:
                res=min(res,helper(x,y+1))
            
            dp[x][y]= res-val if res-val>0 else 1
            return dp[x][y]
        
        
        return helper(0,0)

#https://leetcode.com/problems/dungeon-game/discuss/698271/Python-Short-DP-7-lines-O(mn)-top-down-explained
#space complexity can be reduced
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")]*(n+1) for _ in range(m+1)]
        dp[m-1][n], dp[m][n-1] = 1, 1
            
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        
        return dp[0][0]