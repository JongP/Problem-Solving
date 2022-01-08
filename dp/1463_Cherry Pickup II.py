#unsolved
#I'll be back
#https://leetcode.com/problems/cherry-pickup-ii/discuss/660562/C%2B%2BJavaPython-Top-Down-DP-Clean-code

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp=[[[-1]*n for _ in range(n)] for _ in range(m)]

        @lru_cache(None)
        def dfs(r, c1, c2):
            if r == m: return 0
            if dp[r][c1][c2]!=-1:
                return dp[r][c1][c2]
            
            
            cherries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]
            ans = 0
            for nc1 in range(c1 - 1, c1 + 2):
                for nc2 in range(c2 - 1, c2 + 2):
                    if 0 <= nc1 < n and 0 <= nc2 < n:
                        ans = max(ans, dfs(r + 1, nc1, nc2))
            
            dp[r][c1][c2]=ans+cherries
            
            return ans + cherries

        return dfs(0, 0, n - 1)

#https://leetcode.com/problems/cherry-pickup-ii/discuss/660586/Python-Clean-O(M2N)-dp-10-lines-explained
    def cherryPickup(self, grid):
        M, N = len(grid[0]), len(grid)

        dp = [[[-10**9] * (M+2) for _ in range(M+2)] for _ in range(N)]
        dp[0][1][M] = grid[0][0] + grid[0][M-1]
        for j in range(1, N):
            for i1, i2 in product(range(1, M+1), range(1, M+1)):
                cand_prev = []
                for shift1, shift2 in product([-1,0,1], [-1,0,1]):
                    cand_prev.append(dp[j-1][i1 + shift1][i2 + shift2])
                    dp[j][i1][i2] = (grid[j][i1-1] + grid[j][i2-1])//(1 + (i1 == i2)) + max(cand_prev)

        return max(list(map(max, *dp[-1])))      