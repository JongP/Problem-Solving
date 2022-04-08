class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        """
        #brute force w/ bfs -- simulate
        (0,0)-->next step --> next step --> next step
        until we found (x,y)
        8^(steps)
        
        Q) should we search all nodes <--> can we prune some nodes
        
        
        #method
        subproblem 
        (x,y) = min(dp(x-2,y-1),dp()...   )


        """
        q=collections.deque([(0,0)])
        visited=set()
        step=0
        
        while q :
            
            for _ in range(len(q)):
                cx,cy=q.popleft()
                if (cx,cy)==(x,y): return step
                
                for nx,ny in [(cx+1,cy+2),(cx+2,cy+1),(cx-2,cy-1),(cx-1,cy-2),(cx+1,cy-2),(cx-2,cy+1),(cx-1,cy+2),(cx+2,cy-1)]:
                    if (nx,ny) not in visited:
                        visited.add((nx,ny))
                        q.append((nx,ny))
        
        
            step+=1
        
#https://leetcode.com/problems/minimum-knight-moves/discuss/947138/Python-3-or-BFS-DFS-Math-or-Explanation
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = collections.deque([(0, 0, 0)])
        x, y, visited = abs(x), abs(y), set([(0,0)])
        while q:
            a, b, step = q.popleft()
            if (a, b) == (x,y): return step
            for dx, dy in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1)]:  # no need to have (-1, -2) and (-2, -1) since it only goes 1 direction
                if (a+dx, b+dy) not in visited and -1 <= a+dx <= x+2 and -1 <= b+dy <= y+2:
                    visited.add((a+dx, b+dy))
                    q.append((a+dx, b+dy, step+1))
        return -1 
        
        
        
        
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(None) 
        def dp(x,y):
            if x + y == 0: return 0
            elif x + y == 2: return 2
            return min(dp(abs(x-1),abs(y-2)), dp(abs(x-2),abs(y-1))) + 1
        return dp(abs(x),abs(y))