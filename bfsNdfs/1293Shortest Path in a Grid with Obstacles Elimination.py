from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        if m==1 and n==1: return 0
        visited=[[[False]*(k+1) for _ in range(n)] for _ in range(m)]
        
        
        res=1
        que=deque([(0,0,0)])#mistake
        
        while que:
            
            for _ in range(len(que)):
                x,y,z=que.popleft()
                
                for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                    nx,ny=x+dx,y+dy
                    if nx<0 or nx>=m or ny<0 or ny>=n : continue
                    
                    if (nx,ny) == (m-1,n-1): return res
                    
                    if grid[nx][ny]==0 and not visited[nx][ny][z]:
                        que.append((nx,ny,z))
                        visited[nx][ny][z]=True
                    elif z<k and not visited[nx][ny][z+1]: 
                        que.append((nx,ny,z+1))
                        visited[nx][ny][z+1]=True

        
            res+=1
        
        
        return -1

#optimized
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        if m==1 and n==1: return 0
        visited=[[[False]*(k+1) for _ in range(n)] for _ in range(m)]
        
        
        res=1
        que=deque([(0,0,0)])#mistake
        
        while que:
            
            for _ in range(len(que)):
                x,y,z=que.popleft()
                
                for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                    nx,ny=x+dx,y+dy
                    if nx<0 or nx>=m or ny<0 or ny>=n : continue
                    
                    if (nx,ny) == (m-1,n-1): return res
                    
                    
                    if grid[nx][ny]==0 and not visited[nx][ny][z]:
                        que.append((nx,ny,z))
                        visited[nx][ny][z:]=[True]*(k+1-z)#optimized
                    elif grid[nx][ny]==1 and z<k and not visited[nx][ny][z+1]: 
                        que.append((nx,ny,z+1))
                        visited[nx][ny][z+1:]=[True]*(k-z)#optimized

        
            res+=1
        
        
        return -1

#https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/452434/JavaPython-BFS-Concise-and-Clean-O(m*n*k)
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2: return m + n - 2  # if we can go by manhattan distance -> let's go
        
        DIR = [0, 1, 0, -1, 0]
        q = deque([(0, 0, k)])  # pair of (r, c)
        seen = set()
        seen.add((0, 0, k))
        step = 0
        while q:
            for _ in range(len(q)):
                r, c, k = q.popleft()
                if r == m - 1 and c == n - 1: return step  # Reach to the bottom right cell
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i + 1]
                    if nr < 0 or nr == m or nc < 0 or nc == n: continue  # Skip out of bound cells!
                    newK = k - grid[nr][nc]
                    newState = (nr, nc, newK)
                    if newK >= 0 and newState not in seen:
                        seen.add(newState)
                        q.append(newState)

            step += 1

        return -1