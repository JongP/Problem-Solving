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
    d,cur,level=heapq.heappop(heap)
    if dists[cur][level]<d:
        continue

    for nextt,cost in graph[cur]:
        if dists[nextt][level]>dists[cur][level]+cost:
            dists[nextt][level]=dists[cur][level]+cost
            heapq.heappush(heap,(dists[nextt][level],nextt,level))
        if level>0 and dists[nextt][level-1]>dists[cur][level]:
            dists[nextt][level-1]=dists[cur][level]
            heapq.heappush(heap,(dists[nextt][level-1],nextt,level-1))

print(min(dists[N-1]))



#fastest solution
#https://www.acmicpc.net/source/33079449


import sys; read = sys.stdin.readline
import math; INF = math.inf
from heapq import heappush, heappop

def dijkstra():
    s = 1
    dist = [[INF] * (V+1) for _ in range(K+1)]
    Q = []
    
    for k in range(K+1):
        dist[k][s] = 0             #this can speed up  #almost same execpt for this
    
    init_state = (0, s, 0)
    heappush(Q, init_state)

    while Q:
        d, u, k = heappop(Q)
        if dist[k][u] < d:
            continue
        for v, w in graph[u].items():
            d_new = d + w
            if d_new < dist[k][v]:
                dist[k][v] = d_new
                
                state_new = (d_new, v, k)
                heappush(Q, state_new)
            
            if k < K and d < dist[k+1][v] : # pave
                dist[k+1][v] = d
                
                state_new = (d, v, k+1)
                heappush(Q, state_new)
                
    print(min([dist[k][V] for k in range(K+1)]))

if __name__ == "__main__":
    V, E, K = map(int, read().split())
    graph = [dict() for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, read().split())
        if v in graph[u]:
            graph[u][v] = min(w, graph[u][v])
            graph[v][u] = min(w, graph[v][u])
        else:
            graph[u][v] = w
            graph[v][u] = w

    dijkstra()