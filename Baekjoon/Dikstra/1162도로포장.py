from collections import defaultdict
import heapq
import math
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())



N,M,K=map(int,input().split())

graph=defaultdict(list)
for _ in range(M):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    graph[a].append((b,c))
    graph[b].append((a,c))

dists=[[math.inf]*(K+1) for _ in range(N)]
dists[0][K]=0
heap=[]
heapq.heappush(heap,(0,0,K))

while heap:
    _,cur,level=heapq.heappop(heap)

    for nextt,cost in graph[cur]:
        if dists[nextt][level]>dists[cur][level]+cost:
            dists[nextt][level]=dists[cur][level]+cost
            heapq.heappush(heap,(dists[nextt][level],nextt,level))
        if level>0 and dists[nextt][level-1]>dists[cur][level]:
            dists[nextt][level-1]=dists[cur][level]
            heapq.heappush(heap,(dists[nextt][level-1],nextt,level-1))

print(min(dists[N-1]))