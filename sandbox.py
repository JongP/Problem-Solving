
from collections import deque
import sys
input = sys.stdin.readline


r, c = map(int, input().rstrip().split())

graph=[]
start=0
end=0
for i in range(r):
    row = input().rstrip()
    if 'L' in row:
        if start==0:
            start = (i,row.index('L'))
        else:
            end = (i,row.index('L'))
    graph.append(list(row))

def printGraph():
    for row in graph:
        print(row)
    print("\n\n")

visited = [[0]*c for _ in range(r)]

printGraph()
#bfs
def isReachable(startList,end):
    queue = deque([])
    while startList:
        start = startList.pop()
        queue.append(start)
        visited[start[0]][start[1]]=1

    while queue:
        x,y = queue.popleft()

        if x>0 and graph[x-1][y]!='X' and visited[x-1][y]==0:
            if (x-1,y)==end: return True
            visited[x-1][y]=1
            queue.append((x-1,y))
        if y>0 and graph[x][y-1]!='X' and visited[x][y-1]==0:
            if (x,y-1)==end: return True
            visited[x][y-1]=1
            queue.append((x,y-1))
        if x<r-1 and graph[x+1][y]!='X' and visited[x+1][y]==0:
            if (x+1,y)==end: return True
            visited[x+1][y]=1
            queue.append((x+1,y))
        if y<c-1 and graph[x][y+1]!='X' and visited[x][y+1]==0:
            if (x,y+1)==end: return True
            visited[x][y+1]=1
            queue.append((x,y+1))
    return False

answer = 0
flag= 0 
startList=[start]
while True:
    if(isReachable(startList,end)):
        break

    
    for i in range(r):
        for j in range(c):
            if graph[i][j] !='X' or graph[i][j]==flag: 
                continue

            if i>0 and graph[i-1][j]!='X' and graph[i-1][j]!=flag:
                graph[i][j]=flag
                startList.append((i,j))
            elif i<r-1 and graph[i+1][j]!='X' and graph[i+1][j]!=flag:
                graph[i][j]=flag
                startList.append((i,j))
            elif j>0 and graph[i][j-1]!='X' and graph[i][j-1]!=flag:
                graph[i][j]=flag
                startList.append((i,j))
            elif j<c-1 and graph[i][j+1]!='X' and graph[i][j+1]!=flag:
                graph[i][j]=flag
                startList.append((i,j))
    printGraph()

    flag=1-flag
    answer+=1

print(answer)