class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        res=0
        visited=[[False]*n for _ in range(m)]
        
        
        def goDFS(x,y,visited):
            stk=[(x,y)]
            
            
            while stk:
                cx,cy=stk.pop()
                visited[cx][cy]=True
                
                for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
                    nx,ny=cx+dx,cy+dy
                    if nx<0 or nx>=m or ny<0 or ny>=n or grid[nx][ny]=="0" or visited[nx][ny]: continue
                    stk.append((nx,ny))
                    
            
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and visited[i][j]==False:
                    goDFS(i,j,visited)
                    res+=1
                    
        return res  

#sample fast solution
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m,n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    count += 1
                    
        return count
    
    def dfs(self,grid,i,j):
        m,n = len(grid), len(grid[0])
        grid[i][j] = '0'
        dr = [(0,1),(0,-1),(1,0),(-1,0)]
        for d1,d2 in dr:
            if 0<=i+d1 and i+d1<m and 0<=j+d2 and j+d2<n and grid[i+d1][j+d2]=='1':
                grid[i+d1][j+d2] == '0'
                self.dfs(grid,i+d1,j+d2)
                
#sample stack solution
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])
        
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        curr_row = 0
        count = 0
        for curr_row in range(row):
            for curr_col in range(column):
                val = grid[curr_row][curr_col]
                if val == "1":
                    count += 1
                    stack = [[curr_row, curr_col]]
                    while stack:
                        i, j = stack.pop()
                        grid[i][j] = -1
                        for x, y in direction:
                            new_x = i + x
                            new_y = j + y
                            if row > new_x and new_x >= 0 and column > new_y and new_y >= 0:
                                if grid[new_x][new_y] == "1":
                                    stack.append([new_x, new_y])
        return count