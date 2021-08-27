import heapq
import sys
input =sys.stdin.readline
INF=int(1e9)

T= int(input())
ansList=[]

def dijkstra(start):
    node_set=set()
    dist=[INF]*(n+1)
    heap = [(0,start)]
    dist[start]=0
    

    while heap:
        _,node = heapq.heappop(heap)
        if node in node_set: continue
        
        node_set.add(node)

        if node not in graph: continue
        
        for iter_n in graph[node]:
            if iter_n in node_set: continue
            if graph[node][iter_n] + dist[node] < dist[iter_n]:
                dist[iter_n]= graph[node][iter_n] + dist[node]
                heapq.heappush(heap,(dist[iter_n],iter_n))
    return dist

ansList=[]

for _ in range(T):
    n,m,t = tuple(map(int,input().rstrip().split()))
    s,g,h = tuple(map(int,input().rstrip().split()))
    stray=INF
    graph={}
    goals=[]

    #creating graph
    for _ in range(m):
        n1,n2,wei = tuple(map(int,input().rstrip().split()))

        if (n1==g and n2==h) or (n1==h and n2==g): stray = wei

        if n1 not in graph:
            graph[n1]={n2:wei}
        elif n2 not in graph[n1] or graph[n1][n2]>wei:
            graph[n1][n2]= wei

        if n2 not in graph:
            graph[n2]={n1:wei}
        elif n1 not in graph[n2] or graph[n2][n1]>wei:
            graph[n2][n1]= wei

    #creating goals list
    for _ in range(t):
        goals.append(int(input()))
    goals.sort()

    dijkStart = dijkstra(s)
    dijkG = dijkstra(g)
    dijkH = dijkstra(h)
    
    answers=[]
    for i in goals:
        #route 1: s->g->h->i
        if dijkStart[g]!=INF and dijkH[i]!=INF :
            route1 = dijkStart[g]+stray+dijkH[i]    
        else:
            route1= INF
        #route 2: s->h->g->i
        if dijkStart[h]!=INF and dijkG[i]!=INF :
            route2 = dijkStart[h]+stray+dijkG[i]    
        else:
            route2= INF
        
        if dijkStart[i]>=route1 or dijkStart[i]>=route2:
            answers.append(str(i))
    ansList.append(answers)


#printing out answers
for answers in ansList:
    print(" ".join(answers))