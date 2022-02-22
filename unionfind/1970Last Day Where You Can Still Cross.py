class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        p={}
        
        def find(x):
            if x not in p:
                p[x]=-1
                
            if p[x]<0: return x
            
            p[x]=find(p[x])
            return p[x]
        
        def union(x,y):
            nonlocal col
            
            x=find(x)
            y=find(y)
            if x==y: return False
            
            
            if (x%col==0 and (y+1)%col==0) or (y%col==0 and (x+1)%col==0):
                return True
            elif x%col==0 or (x+1)%col==0: 
                p[y]=x
            else:
                p[x]=y
            
            return False
        
        res=0
        for x,y in cells:
            x-=1;y-=1;
            curID= x*col+y
            
            if curID not in p: #what I forgot
                p[curID]=-1
            
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]:
                nx,ny=x+dx,y+dy
                if nx<0 or nx>=row or ny<0 or ny>=col or nx*col+ny not in p: continue
                if union(curID,nx*col+ny):
                    return res

                
            res+=1
            
        return res



#reverse iterate
# #https://leetcode.com/problems/last-day-where-you-can-still-cross/discuss/1403930/Python-Union-Find-solution-explained
class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution:
    def latestDayToCross(self, n, m, C):
        row, col = len(C), len(C[0])
        dsu = DSU(m*n + 2)
        grid = [[1] * m for _ in range(n)]
        neibs = [[0,1],[0,-1],[1,0],[-1,0]]
        C = [(x-1, y-1) for x, y in C]

        def index(x, y):
            return x * m + y + 1

        for i in range(len(C) - 1, -1, -1):
            x, y = C[i][0], C[i][1]

            grid[x][y] = 0
            for dx, dy in neibs:
                ind = index(x+dx, y+dy)
                if x+dx>=0 and x+dx<n and y + dy >= 0 and y + dy < m and grid[x+dx][y+dy] == 0:
                    dsu.union(ind, index(x, y))
            if x == 0:
                dsu.union(0, index(x, y))
            if x == n - 1:
                dsu.union(m*n + 1, index(x, y))

            if dsu.find(0) == dsu.find(m*n + 1):
                return i

#binary search
#https://leetcode.com/problems/last-day-where-you-can-still-cross/discuss/1403907/C%2B%2BJavaPython-Binary-Search-and-BFS-Clean-and-Concise
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        DIR = [0, 1, 0, -1, 0]

        def canWalkFromTopToBottom(dayAt):
            grid = [[0] * col for _ in range(row)]  # Create grid in the `dayAt` th date
            for i in range(dayAt):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1  # Mark as water

            bfs = deque([])
            for c in range(col):
                if grid[0][c] == 0:  # Add all valid start cells in the top row
                    bfs.append((0, c))
                    grid[0][c] = 1  # Mark as visited

            while bfs:
                r, c = bfs.popleft()
                if r == row - 1: return True  # Reach to bottom -> Return Valid
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i + 1]
                    if nr < 0 or nr == row or nc < 0 or nc == col or grid[nr][nc] == 1: continue
                    grid[nr][nc] = 1  # Mark as visited
                    bfs.append((nr, nc))
            return False

        left, right = 1, len(cells)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if canWalkFromTopToBottom(mid):
                ans = mid  # Update current answer so far
                left = mid + 1  # Try to find a larger day
            else:
                right = mid - 1  # Try to find a smaller day
        return ans