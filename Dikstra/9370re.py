import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dikstra(graph,n,start):
    dists = [INF]*(n+1)
    nodes = set()

    heap = [(0,start)]

    while heap:
        dist, node = heapq.heappop(heap)
        if node in nodes:
            continue

        nodes.add(node)
        dists[node] = dist

        if node not in graph:
            continue

        for next_node in graph[node]:
            if next_node in nodes:
                continue
            new_dist = dists[node] + graph[node][next_node]

            if dists[next_node]> new_dist :
                dists[next_node] = new_dist
                heapq.heappush(heap,(new_dist,next_node))
    
    return dists



t= int(input())
ansList=[]
for _ in range(t):
    answer = []
    n,m,t = map(int,input().rstrip().split())
    s,g,h = map(int,input().rstrip().split())
    

    #making graph
    graph={}
    for _ in range(m):
        a,b,c = map(int,input().rstrip().split())

        if a not in graph:
            graph[a]= {b:c}
        else :
            graph[a][b]=c
        
        if b not in graph:
            graph[b]= {a:c}
        else :
            graph[b][a]=c
    
    #candidates
    candidates=[]
    for _ in range(t):
        candidates.append(int(input()))
    
    distsS = dikstra(graph,n,s)

    
    for candidate in candidates:
        distsC = dikstra(graph,n,candidate)

        if distsC[s] == INF:
            continue
        distSC = distsC[s]
        distSHGC = distsS[h] + graph[h][g] + distsC[g]
        distSGHC = distsS[g] + graph[h][g] + distsC[h]

        if distSC == distSGHC or distSC == distSHGC:
            answer.append(candidate)
    
    answer.sort()
    ansList.append(" ".join(list(map(str,answer))))





for answer in ansList:
    print(answer)