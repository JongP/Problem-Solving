import heapq
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())


m,n=map(int,input().split())
#(n,m)
graph=[input() for _ in range(n)]
visited=[[False]*m for _ in range(n)]
dists=[[int(2e9)]*m for _ in range(n)]
dists[0][0]=1
heap=[]
heapq.heappush(heap,(0,0,0))

while heap:
    d,cx,cy=heapq.heappop(heap)
    if visited[cx][cy]:
        continue
    if (cx,cy)==(n-1,m-1):
        print(d)
        exit()
    visited[cx][cy]=True

    for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
        nx,ny=cx+dx,cy+dy
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        
        newD=d+1 if graph[nx][ny]=="1" else d
        if dists[nx][ny]>newD:
            dists[nx][ny]=newD
            heapq.heappush(heap,(newD,nx,ny))

