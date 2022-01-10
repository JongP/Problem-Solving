from collections import defaultdict
import heapq
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
INF=int(1e9)


n,m,t,d=map(int,input().split())
graph=[]
for i in range(n):
    line=input()
    for char in line:
        if ord(char)-97>=0:
            graph.append(ord(char)-97+26)
        else:
            graph.append(ord(char)-65)


#to go dikstra
visited=[[False]*m for _ in range(n)]
dists=[[INF]*m for _ in range(n)]
dists[0][0]=0
heap=[]
heapq.heappush(heap,(0,0,0))

while heap:
    dist,cx,cy=heapq.heappop(heap)
    if visited[cx][cy]:
        continue

    visited[cx][cy]=True

    for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
        nx,ny=cx+dx,cy+dy
        if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny] or abs(graph[nx][ny]-graph[cx][cy])>t:
            continue

        newDist=dist
        if graph[nx][ny]<=graph[cx][cy]:
            newDist+=1
        else:
            newDist+=(graph[nx][ny]-graph[cx][cy])**2

        if newDist<dists[nx][ny]:
            dists[nx][ny]=newDist
            heapq.heappush(heap,(newDist,nx,ny))



#to come dikstra
visited=[[False]*m for _ in range(n)]
backDists=[[INF]*m for _ in range(n)]
backDists[0][0]=0
heap=[]
heapq.heappush(heap,(0,0,0))

while heap:
    dist,cx,cy=heapq.heappop(heap)
    if visited[cx][cy]:
        continue

    visited[cx][cy]=True

    for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
        nx,ny=cx+dx,cy+dy
        if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny] or abs(graph[nx][ny]-graph[cx][cy])>t:
            continue

        newDist=dist
        if graph[nx][ny]>graph[cx][cy]:
            newDist+=1
        else:
            newDist+=(graph[nx][ny]-graph[cx][cy])**2

        if newDist<backDists[nx][ny]:
            backDists[nx][ny]=newDist
            heapq.heappush(heap,(newDist,nx,ny))


res=graph[0][0]
for i in range(n):
    for j in range(m):
        if dists[i][j]+backDists[i][j]>d:
            continue
        if graph[i][j]>res:
            res=graph[i][j]
print(res)
