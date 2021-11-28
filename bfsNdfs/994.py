class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:    
        m=len(grid)
        n=len(grid[0])
        dxdy=((0,1),(0,-1),(1,0),(-1,0))

        leftNum=0
        ans=0

        que=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    que.append((i,j))
                elif grid[i][j]==1:
                    leftNum+=1
        
        if not leftNum:
            return 0
        
        while que:
            l=len(que)

            for _ in range(l):
                cX,cY=que.popleft()

                for dx, dy in dxdy:
                    nX,nY=cX+dx,cY+dy
                    if nX<0 or nX>=m or nY<0 or nY>=n:
                        continue

                    if grid[nX][nY]==1:
                        grid[nX][nY]=2
                        leftNum-=1
                        que.append((nX,nY))
            ans+=1

        print(leftNum)

        if not leftNum:
            return ans-1
        else:
            return -1