import heapq
import sys
input =sys.stdin.readline

T= int(input())
ansList=[]

def dijkstra(start):
    node_set=set()
    dist=[sys.maxsize]*(n+1)
    heap = [(0,start)]
    dist[start]=0
    

    while heap:
        _,node = heapq.heappop(heap)
        if node in node_set: continue
        
        node_set.add(node)

        if node not in graph: continue
        
        for iter_w ,iter_n in graph[node]:
            if iter_n in node_set: continue
            if iter_w + dist[node] < dist[iter_n]:
                dist[iter_n]= iter_w + dist[node]
                heapq.heappush(heap,(dist[iter_n],iter_n))
    return dist

ansList=[]

for _ in range(T):
    n,m,t = tuple(map(int,input().rstrip().split()))
    s,g,h = tuple(map(int,input().rstrip().split()))
    stray=0
    graph={}
    goals=[]

    #creating graph
    for _ in range(m):
        n1,n2,wei = tuple(map(int,input().rstrip().split()))

        if (n1==g and n2==h) or (n1==h and n2==g): stray=wei

        if n1 not in graph:
            graph[n1]=[(wei,n2)]
        else:
            graph[n1].append((wei,n2))

        if n2 not in graph:
            graph[n2]=[(wei,n1)]
        else:
            graph[n2].append((wei,n1))

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
        if dijkStart[g]!=sys.maxsize and dijkH[i]!=sys.maxsize:
            route1 = dijkStart[g]+stray+dijkH[i]    
        else:
            route1= sys.maxsize
        #route 2: s->h->g->i
        if dijkStart[h]!=sys.maxsize and dijkG[i]!=sys.maxsize:
            route2 = dijkStart[h]+stray+dijkG[i]    
        else:
            route2= sys.maxsize

        if dijkStart[i]>=route1 or dijkStart[i]>=route2:
            answers.append(str(i))
    ansList.append(answers)


#printing out answers
for answers in ansList:
    print(" ".join(answers))