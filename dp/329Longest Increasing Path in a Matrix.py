class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        res=1
        
        
        dp=[[-1]*n for _ in range(m)]
        
        def dfs(x,y):
            nonlocal res
            
            if dp[x][y]!=-1:
                return dp[x][y]
            
            val=0
            
            for nx,ny in [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]:
                if nx<0 or nx>=m or ny<0 or ny>=n or matrix[nx][ny]<=matrix[x][y]: continue
                if dp[nx][ny]==-1:
                    dfs(nx,ny)
                
                if val<dp[nx][ny]:
                    val=dp[nx][ny]
            
            
            dp[x][y]=val+1
            
            if dp[x][y]>res: res=dp[x][y]

        
        for i in range(m):
            for j in range(n):
                if dp[i][j]==-1:
                    dfs(i,j)
        
        return res


#https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78334/Python-solution-memoization-dp-288ms
    def longestIncreasingPath(self, matrix):
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))


#
#topological sorgin
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        DIR = [0, 1, 0, -1, 0]
        m, n = len(matrix), len(matrix[0])
        
        outDegree = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or matrix[nr][nc] <= matrix[r][c]: continue
                    outDegree[r][c] += 1
            
        q = deque([])
        for r in range(m):
            for c in range(n):
                if outDegree[r][c] == 0:
                    q.append([r, c])
                    
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or matrix[nr][nc] >= matrix[r][c]: continue
                    outDegree[nr][nc] -= 1
                    if outDegree[nr][nc] == 0:
                        q.append([nr, nc])
                    
        return level   