from collections import deque
class Solution:
    def updateMatrix(self, mat):
        m=len(mat)
        n=len(mat[0])
        INF=int(1e9)
        
        ans=[[INF]*n for _ in range(m)]
        visited=[[0]*n for _ in range(m)]
        dxdy=((0,1),(0,-1),(-1,0),(1,0))


        queue=deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    ans[i][j]=0
                    queue.append((i,j))
                    visited[i][j]=1
        
        depth=1
        while queue:
            l=len(queue)
            for _ in range(l):
                curX,curY=queue.popleft()
                
                for dx,dy in dxdy:
                    nX,nY=curX+dx,curY+dy
                    if nX<0 or nX>=m or nY<0 or nY>=n:
                        continue
                    if visited[nX][nY]==0:
                        ans[nX][nY]=depth
                        visited[nX][nY]=1
                        queue.append((nX,nY))
                
            depth+=1
        
                
        return ans