# 1504번: 특정한 최단 경로
# 1 -> N 
# 두 정점을 이용 할 것
from collections import deque
import sys

def BFS( start ):
    global N
    dist = [ 123456789 for i in range(N+1) ]
    dist[start] = 0
    
    queue = deque()
    queue.append( [start, 0] )
    while queue:
        node, cost = queue.popleft()
        
        if dist[node] != cost: continue
        for nextNode in range(1, N+1):
            if dist[nextNode] > dist[node] + graph[node][nextNode]:
                dist[nextNode] = dist[node] + graph[node][nextNode]
                queue.append( [nextNode, dist[nextNode]] )                
    return dist        
#############################################################################
N, E = list(map(int, input().split()))
graph = [ [123456789]*(N+1) for i in range(N+1) ]
for i in range(E):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    graph[a][b] = graph[b][a] = min(graph[a][b], c)
v1, v2 = list(map(int, input().split()))

d1 = BFS(1)
d2 = BFS(v1)
d3 = BFS(v2)

result = min( 
    d1[v1] + d2[v2] + d3[N], # 1 -> v1 -> v2 -> N
    d1[v2] + d3[v1] + d2[N] # 1 -> v2 -> v1 -> N
)
if result >= 123456789: print( -1 )
else: print( result )