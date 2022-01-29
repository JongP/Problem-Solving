class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid), len(obstacleGrid[0])
        
        prev=[0]*(n+1)
        cur=[0]*(n+1)
        for j in range(n):
            if obstacleGrid[0][j]==1:break
            prev[j+1]=1
        #print(prev)
        for i in range(1,m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    cur[j+1]=0
                else: 
                    cur[j+1]=cur[j]+prev[j+1]
            
            #print(cur)
            prev,cur=cur,prev
            
        
        
        return prev[-1]#miunderstood





#https://leetcode.com/problems/unique-paths-ii/discuss/23410/Python-different-solutions-(O(m*n)-O(n)-in-place)
# O(n) space
def uniquePathsWithObstacles2(self, obstacleGrid):
    if not obstacleGrid:
        return 
    r, c = len(obstacleGrid), len(obstacleGrid[0])
    cur = [0] * c
    cur[0] = 1 - obstacleGrid[0][0]
    for i in xrange(1, c):
        cur[i] = cur[i-1] * (1 - obstacleGrid[0][i])
    for i in xrange(1, r):
        cur[0] *= (1 - obstacleGrid[i][0])
        for j in xrange(1, c):
            cur[j] = (cur[j-1] + cur[j]) * (1 - obstacleGrid[i][j])
    return cur[-1]

# in place
def uniquePathsWithObstacles(self, obstacleGrid):
    if not obstacleGrid:
        return 
    r, c = len(obstacleGrid), len(obstacleGrid[0])
    obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
    for i in xrange(1, r):
        obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1 - obstacleGrid[i][0])
    for i in xrange(1, c):
        obstacleGrid[0][i] = obstacleGrid[0][i-1] * (1 - obstacleGrid[0][i])
    for i in xrange(1, r):
        for j in xrange(1, c):
            obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) * (1 - obstacleGrid[i][j])
    return obstacleGrid[-1][-1]