from collections import defaultdict
import heapq
import math
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
INF=int(1e9)


def pathDikstra(graph,S,D,N):
    dists=[math.inf]*N
    dists[S]=0
    path=[[-1] for _ in range(N)]
    heap=[]
    heapq.heappush(heap,(0,S))
    
    while heap:
        d,cur=heapq.heappop(heap)
        if d>dists[cur]:
            continue

        for nextt,cost in graph[cur].items():
            if dists[nextt]>d+cost:
                dists[nextt]=d+cost
                path[nextt].clear()
                path[nextt].append(cur)
                heapq.heappush(heap,(dists[nextt],nextt))
            elif dists[nextt]==d+cost:
                path[nextt].append(cur)

    visited=set()
    trav=[D]
    while trav:
        cur=trav.pop()

        visited.add(cur)
        for nt in path[cur]:
            if nt==-1:
                 continue
  
            graph[nt][cur]=int(1e9)
            if nt not in visited:
                trav.append(nt)

    return


N,M=map(int,input().split())

while (N,M)!=(0,0):
    S,D=map(int,input().split())
    
    graph=defaultdict(dict)
    for _ in range(M):
        a,b,c=map(int,input().split())
        graph[a][b]=c



    visited = pathDikstra(graph,S,D,N)



    dists=[math.inf]*N
    dists[S]=0
    heap=[]
    heapq.heappush(heap,(0,S))
    while heap:
        d,cur= heapq.heappop(heap)
        if d>dists[cur]:
            continue

        for nextt,cost in graph[cur].items():
            if cost==int(1e9):
                continue
            if dists[nextt]>d+cost:
                dists[nextt]=d+cost
                heapq.heappush(heap,(dists[nextt],nextt))
        
    if dists[D]==math.inf:
        print(-1)
    else:
        print(dists[D])

    N,M=map(int,input().split())




#https://www.acmicpc.net/source/28099092
#how to rebuild the path with backtracking
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
def dijkstra(start,end,graph):

    distance = [INF] * (N+1)

    pq = []

    distance[start] = 0

    heapq.heappush(pq,(distance[start],start))

    while pq:

        currentDist, currentNode = heapq.heappop(pq)

        if distance[currentNode] < currentDist: continue

        for nextNode in graph[currentNode]:

            nextDist = currentDist + graph[currentNode][nextNode]

            if nextDist < distance[nextNode]:
                distance[nextNode] = nextDist
                heapq.heappush(pq,(nextDist,nextNode))
             
        if currentNode == end:
            break
    
    return distance

def backtraking(graph,end):
    temp = distance[end]
    #print(temp)

    for i in where[end]:
        if distance[i] > distance[end]:
            continue

        elif distance[i] + graph[i][end] == temp:
            if (i,end) not in delete:
                delete.add((i,end))
                backtraking(graph,i)








while True:
    N, M = list(map(int, list(input().split())))

    if N + M == 0:
        quit()


    graph = [{} for _ in range(N+1)]
    where = [[] for _ in range(N+1)]
    S, D = list(map(int,list(input().split())))

    for _ in range(M):
        U, V, P = list(map(int,list(input().split())))

        graph[U][V] = P
        where[V].append(U) # 한 정점에 모이는 다른 정점을 보기위해 만듬.

    delete = set()

    distance = dijkstra(S,D,graph)
    backtraking(graph,D)

    for a,b in delete:
        del graph[a][b]

    temp = dijkstra(S,D,graph)[D]

    if temp == INF :
        print(-1)
    else:
        print(temp)