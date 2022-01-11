from collections import defaultdict
import heapq
import math
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
INF=int(1e9)

n,m,d,e=map(int,input().split())
nodes=list(map(int,input().split()))


upGraph=defaultdict(list)
for _ in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    if nodes[a]==nodes[b]:
        continue
    elif nodes[a]<nodes[b]:
        a,b=b,a
    #a>b
    upGraph[b].append((a,c))
    #downGraph[a].append((b,n))


if n==2:
    print("Impossible")
    exit()

def dikstra(graph,start):
    distances=[math.inf]*n
    distances[start]=0
    visited=[False]*n
    heap=[]
    heapq.heappush(heap,(0,start))

    while heap:
        dist,cur = heapq.heappop(heap)
        if visited[cur]:
            continue

        visited[cur]=True

        for nextt, cost in graph[cur]:
            if visited[nextt]:
                continue
            
            if distances[nextt] > dist+cost*d:
                distances[nextt]=dist+cost*d
                heapq.heappush(heap,(distances[nextt],nextt))

    return distances

goDist=dikstra(upGraph,0)
downDist=dikstra(upGraph,n-1)
    
res=-1*math.inf

for i in range(n):
    if goDist[i]==math.inf or downDist[i]==math.inf:
        continue
    tmp=nodes[i]*e-(goDist[i]+downDist[i])
    if tmp>res:
        res=tmp


if res==-1*math.inf:
    print("Impossible")
else:
    print(res)