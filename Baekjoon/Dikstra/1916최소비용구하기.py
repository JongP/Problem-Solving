from collections import defaultdict
import heapq
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())

n=int(input())
m=int(input())
graph=defaultdict(list)
for _ in range(m):
    d,a,c=map(int,input().split())
    graph[d].append((a,c))

a,b=map(int,input().split())


heap=[]
visited=set()
dists=[int(2e9)]*(n+1)
heapq.heappush(heap,(0,a))


while heap:
    dist,cur=heapq.heappop(heap)
    if cur in visited:
        continue

    if cur==b:
        print(dist)
        exit()
    
    dists[cur]=dist
    visited.add(cur)

    for nextt,cost in graph[cur]:
        if nextt in visited:
            continue

        if dists[nextt]>dist+cost:
            dists[nextt]=dist+cost
            heapq.heappush(heap,(dists[nextt],nextt))

    