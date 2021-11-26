from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[0]*n for _ in range(m)]
        
        
        def goBFS(x,y):
            queue=deque()
            tmp=0
            queue.append((x,y))
            
            while queue:
                curX,curY=queue.popleft()
                if visited[curX][curY]==1:
                    continue
                visited[curX][curY]=1
                tmp+=1
                
                for dx,dy in dxdy:
                    newX=curX+dx
                    newY=curY+dy
                    if newX<0 or newX>=m:
                        continue
                    if newY<0 or newY>=n:
                        continue
                    if grid[newX][newY]==1 and visited[newX][newY]==0:
                        queue.append((newX,newY))
                
                
            return tmp
        
        dxdy=[(0,1),(0,-1),(-1,0),(1,0)]
        
        answer=0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and visited[i][j]==0:
                    tmp=goBFS(i,j)
                    if tmp>answer:
                        answer=tmp
        

        
        
        
        return answer