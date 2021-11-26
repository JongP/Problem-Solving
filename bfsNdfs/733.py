from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        dxdy=[(0,1),(0,-1),(1,0),(-1,0)]
        lRow=len(image)
        lCol=len(image[0])
        tColor=image[sr][sc]
        
        
        visited=[[0]*lCol for _ in range(lRow)]
        
        queue=deque()
        queue.append((sr,sc))
        
        while queue:
            curR,curC = queue.popleft()
            if visited[curR][curC]:
                continue
                
            visited[curR][curC]=1
            image[curR][curC]=newColor
            
            for dx ,dy in dxdy:
                if curR+dx<0 or curR+dx>=lRow:
                    continue
                if curC+dy<0 or curC+dy>=lCol:
                    continue
                    
                if  image[curR+dx][curC+dy]==tColor and visited[curR+dx][curC+dy] ==0:
                    queue.append((curR+dx,curC+dy))
            
            
        return image