from collections import deque
import heapq
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())

n=int(input())
graph=[]
for i in range(n):
    line=input()
    for j in range(n):
        if line[j]=="A":
            start=(i,j)
        elif line[j]=="B":
            end=(i,j)
    graph.append(line)

visited=[[False]*n for _ in range(n)]
dists=[[int(2e9)]*n for _ in range(n)]
dists[start[0]][start[1]]=0
path=[[set() for _ in range(n)] for _ in range(n)]
for i in range(4):
    path[start[0]][start[1]].add(i)
dxdy=[(-1,0),(0,1),(1,0),(0,-1)]#n,e,s,w
heap=[]
heapq.heappush(heap,(0,start[0],start[1]))


while heap:
    cd,cx,cy=heapq.heappop(heap)
    if dists[cx][cy]<cd:
        continue

    for i in range(4):
        nx,ny=cx+dxdy[i][0],cy+dxdy[i][1]
        if nx<0 or nx>=n or ny<0 or ny>=n  or graph[nx][ny]=="x":
            continue
        

        newCost=cd + (0 if i in path[cx][cy] else 1)

        if newCost<dists[nx][ny]:
            dists[nx][ny]=newCost
            path[nx][ny].clear()
            path[nx][ny].add(i)
            heapq.heappush(heap,(newCost,nx,ny))
        elif newCost==dists[nx][ny]:
            path[nx][ny].add(i)


print((dists[end[0]][end[1]] if dists[end[0]][end[1]]!=int(2e9) else -1 ))