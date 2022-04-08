class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        """
        #1 brute force
        for every single hit, check stable bricks w/ graph searching(dfs/bfs)
        --> O(len(hits)*m*n   )
        
        
        """
        m,n=len(grid),len(grid[0])
        res=[]
        
        #reset the map
        invalid=set()
        for hX,hY in hits:
            if grid[hX][hY]==0:
                invalid.add((hX,hY))
            grid[hX][hY]=0
        
        p=[-1]*(m*n+1)
            
        #Union Find
        def find(x):
            if p[x]<0:
                return x
            p[x]=find(p[x])
            return p[x]
        
        def union(x,y):
            x,y=find(x),find(y)
            if x==y: return 0
            
            
            if y==m*n:
                x,y=y,x
            
            val=p[y]
            
            p[x]+=p[y]
            p[y]=x
            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if i==0:
                        union(i*n+j,m*n)
                    
                    for nx,ny in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                            union(i*n+j,nx*n+ny)
        
        
        
        #reverse time
        res=[]
        
        for i,j in reversed(hits): 
            if (i,j) in invalid: 
                res.append(0)
                continue
                
            grid[i][j]=1
            val=-p[m*n]
            isStable=False if i!=0 else True
            if i==0:
                union(i*n+j,m*n)
            
            for nx,ny in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                    #tmp=find(nx*n+ny)
                    union(nx*n+ny,i*n+j)
            
            res.append(max(0,-p[m*n]-val-1))
            
            
        res.reverse()
        return res