class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        p=self.defineIsland(grid)
        ret=self.findMax(grid,p)
        
        return ret
    
    
    def defineIsland(self,grid):
        n=len(grid)
        p=[-1]*(n*n)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0: continue
                cur=i*n+j
                for nx,ny in [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]:
                    if nx<0 or nx>=n or ny<0 or ny>=n or grid[nx][ny]==0:
                        continue
                    self.union(p,cur,nx*n+ny)
        
        return p
    
    def findMax(self,grid,p):
        n=len(grid)
        res=1
        for x in range(n):
            for y in range(n):
                if grid[x][y]==1:
                    if -p[x*n+y]>res:
                        res=-p[x*n+y]
                    continue
                
                visited=set()
                
                val=1
                for nx,ny in [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]:
                    if nx<0 or nx>=n or ny<0 or ny>=n or grid[nx][ny]==0: continue
                    parent=self.find(p,nx*n+ny)
                    if parent not in visited:
                        visited.add(parent)
                        val-=p[parent]
                        
                if val>res:
                    res=val        
        
        return res
        
    def find(self,p,x):
        
        if p[x]<0:
            return x
        
        p[x]=self.find(p,p[x])
        
        return p[x]
        
    def union(self,p,x,y):
        x,y=self.find(p,x),self.find(p,y)
        if x==y: return
        

        p[x]+=p[y]
        p[y]=x
        
        return
        
#DFS. union find necessary?
#https://leetcode.com/problems/making-a-large-island/discuss/127032/C%2B%2BJavaPython-Straight-Forward-O(N2)-with-Explanations

    def largestIsland(self, grid):
        N = len(grid)

        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j

        def dfs(x, y, index):
            res = 0
            grid[x][y] = index
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res + 1

        # DFS every island and give it an index of island
        index = 2
        areas = {0: 0}
        for x in xrange(N):
            for y in xrange(N):
                if grid[x][y] == 1:
                    areas[index] = dfs(x, y, index)
                    index += 1

        # traverse every 0 cell and count biggest island it can conntect
        res = max(areas.values())
        for x in xrange(N):
            for y in xrange(N):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y))
                    res = max(res, sum(areas[index] for index in possible) + 1)
        return res

class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [0] * n
    def isExist(self, u):
        return self.parent[u] >= 0
    def add(self, u):
        if self.isExist(u): return  # Only add if not existed yet!
        self.parent[u] = u
        self.size[u] = 1
    def find(self, u):
        if self.parent[u] == u: return u
        self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        if self.size[pu] <= self.size[pv]:  # Merge the smaller component to the bigger component
            self.parent[pu] = pv  # Merge u into v
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu  # Merge v into u
            self.size[pu] += self.size[pv]
        return True

#Union find
#https://leetcode.com/problems/making-a-large-island/discuss/1375992/C%2B%2BPython-DFS-paint-different-colors-Union-Find-Solutions-with-Picture-Clean-and-Concise
class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [0] * n
    def isExist(self, u):
        return self.parent[u] >= 0
    def add(self, u):
        if self.isExist(u): return  # Only add if not existed yet!
        self.parent[u] = u
        self.size[u] = 1
    def find(self, u):
        if self.parent[u] == u: return u
        self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        if self.size[pu] <= self.size[pv]:  # Merge the smaller component to the bigger component
            self.parent[pu] = pv  # Merge u into v
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu  # Merge v into u
            self.size[pu] += self.size[pv]
        return True

# O(M * N * α(M*N) ~ O(M * N)
class Solution: 
    def largestIsland(self, grid: List[List[int]]) -> int:
        DIR = [0, 1, 0, -1, 0]
        m, n, ans = len(grid), len(grid[0]), 0
        uf = UnionFind(m * n)

        def landNeighbors(r, c):
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                neiId = nr * n + nc
                if nr < 0 or nr == m or nc < 0 or nc == n or not uf.isExist(neiId): continue
                yield neiId

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0: continue
                curId = r * n + c
                uf.add(curId)
                for neiId in landNeighbors(r, c):
                    uf.union(curId, neiId)
                p = uf.find(curId)
                ans = max(ans, uf.size[p])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: continue
                neiParents = set()
                for neiId in landNeighbors(r, c):
                    neiParents.add(uf.find(neiId))
                sizeFormed = 1  # Start with 1, which is matrix[r][c] when turning from 0 into 1
                for p in neiParents:
                    sizeFormed += uf.size[p]
                ans = max(ans, sizeFormed)
        return ans

# Complexity

# Time: O(M * N * α(M*N) ~ O(M * N), where M <= 500 is number of rows, N <= 500 is number of columns in the matrix.
# Explanation: Using both path compression and union by size ensures that the amortized time per operation is only α(n), which is optimal, where α(n) is the inverse Ackermann function. This function has a value α(n) < 5 for any value of n that can be written in this physical universe, so the disjoint-set operations take place in essentially constant time.
# Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure or https://www.slideshare.net/WeiLi73/time-complexity-of-union-find-55858534 for more information.
# Space: O(M * N)