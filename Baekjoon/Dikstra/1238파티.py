from collections import defaultdict
import heapq
import sys
input=lambda: sys.stdin.readline().rstrip()
INF=int(2e9)

n,m,x=map(int,input().split())
x-=1

graph=defaultdict(list)
backGraph=defaultdict(list)
for _ in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    graph[a].append((b,c))
    backGraph[b].append((a,c))

dists=[INF]*n
backDists=[INF]*n

def dikstra(graph,distances,start):
    visited=set()
    heap=[]
    distances[start]=0
    heapq.heappush(heap,(0,start))

    while heap:
        _,cur=heapq.heappop(heap)
        if cur in visited:
            continue

        visited.add(cur)

        for nextt,cost in graph[cur]:
            if nextt in visited:
                continue
            if distances[nextt]>distances[cur]+cost:
                distances[nextt] = distances[cur]+cost
                heapq.heappush(heap,(distances[nextt],nextt))


#first dik
dikstra(graph,dists,x)

#second dik
dikstra(backGraph,backDists,x)

print(max(map(sum,zip(dists,backDists))))