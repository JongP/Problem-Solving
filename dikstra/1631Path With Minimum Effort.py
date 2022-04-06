from heapq import heappush,heappop


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row,col=len(heights),len(heights[0])
        
        visited=set()
        heap=[(0,(0,0))]
        
        
        while heap:
            cost,(cx,cy) = heappop(heap)
            if (cx,cy) in visited: continue
            
            if (cx,cy)==(row-1,col-1):
                return cost
            
            
            visited.add((cx,cy))
            
            
            for nx,ny in [(cx+1,cy),(cx-1,cy),(cx,cy+1),(cx,cy-1)]:
                if 0<=nx<row and 0<=ny<col and (nx,ny) not in visited:
                    heappush(heap,( max(cost,abs(heights[nx][ny]-heights[cx][cy]))   , (nx,ny))   )
                    
#https://leetcode.com/problems/path-with-minimum-effort/discuss/909017/JavaPython-Dijikstra-Binary-search-Clean-and-Concisehttps://leetcode.com/problems/path-with-minimum-effort/discuss/909017/JavaPython-Dijikstra-Binary-search-Clean-and-Concise
class Solution(object):
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        DIR = [0, 1, 0, -1, 0]
        
        def dfs(r, c, visited, threadshold):
            if r == m-1 and c == n-1: return True # Reach destination
            visited[r][c] = True
            for i in range(4):
                nr, nc = r+DIR[i], c+DIR[i+1]
                if nr < 0 or nr == m or nc < 0 or nc == n or visited[nr][nc]: continue
                if abs(heights[nr][nc]-heights[r][c]) <= threadshold and dfs(nr, nc, visited, threadshold): return True
            return False
        
        def canReachDestination(threadshold):
            visited = [[False] * n for _ in range(m)]
            return dfs(0, 0, visited, threadshold)
        
        left = 0
        ans = right = 10**6
        while left <= right:
            mid = left + (right-left)/2
            if canReachDestination(mid):
                right = mid - 1 # Try to find better result on the left side
                ans = mid
            else:
                left = mid + 1
        return ans