import sys
input = sys.stdin.readline
from collections import deque

ansList=[]

def BFS(x,y):
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()

        if x>0 and graph[x-1][y]==1 and visited[x-1][y]==0:
            visited[x-1][y]=1
            queue.append((x-1,y))

        if y>0 and graph[x][y-1]==1 and visited[x][y-1]==0:
            visited[x][y-1]=1
            queue.append((x,y-1))

        if x<h-1 and graph[x+1][y]==1 and visited[x+1][y]==0:
            visited[x+1][y]=1
            queue.append((x+1,y))

        if y<w-1 and graph[x][y+1]==1 and visited[x][y+1]==0:
            visited[x][y+1]=1
            queue.append((x,y+1))

        if x>0 and y>0 and graph[x-1][y-1]==1 and visited[x-1][y-1]==0:
            visited[x-1][y-1]=1
            queue.append((x-1,y-1))
 
        if x>0 and y<w-1 and graph[x-1][y+1]==1 and visited[x-1][y+1]==0:
            visited[x-1][y+1]=1
            queue.append((x-1,y+1))

        if x<h-1 and y>0 and graph[x+1][y-1]==1 and visited[x+1][y-1]==0:
            visited[x+1][y-1]=1
            queue.append((x+1,y-1))

        if x<h-1 and y<w-1 and graph[x+1][y+1]==1 and visited[x+1][y+1]==0:
            visited[x+1][y+1]=1
            queue.append((x+1,y+1))        


w,h= map(int,input().rstrip().split())
while (w,h)!=(0,0) :

    graph = []
    for _ in range(h):
        graph.append(list(map(int,input().rstrip().split())))
    
    visited=[[0]*w for _ in range(h)]
    
    answer=0
    for i in range(h):
        for j in range(w):
            if graph[i][j]==0 or visited[i][j]==1: continue
            answer+=1
            BFS(i,j)
    ansList.append(answer)

    w,h = map(int,input().rstrip().split())

for answer in ansList:
    print(answer)