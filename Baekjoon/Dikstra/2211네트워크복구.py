from collections import defaultdict
import heapq
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())


n,m=map(int,input().split())
graph=defaultdict(list)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


dists=[int(2e9)]*(n+1)
visited=[False]*(n+1)
heap=[]
heapq.heappush(heap,(0,1,0))
res=[]
while heap:
    dist,cur,prev=heapq.heappop(heap)
    if visited[cur] :
        continue
    res.append((cur,prev))
    visited[cur]=True

    for nextt,cost in graph[cur]:
        if visited[nextt]:
            continue
        
        if dist+cost<dists[nextt]:
            dists[nextt]=dist+cost
            heapq.heappush(heap,(dists[nextt],nextt,cur))


print(len(res)-1)
[print(el[0],el[1]) for el in res[1:]]