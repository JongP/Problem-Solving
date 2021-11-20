import heapq
import sys
input =sys.stdin.readline

T= int(input())
ansList=[]

def dijkstra(start):
    node_set=set()
    dist=[20000000000]*(n+1)
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
    stray=sys.maxsize
    graph={}
    goals=[]

    #creating graph
    for _ in range(m):
        n1,n2,wei = tuple(map(int,input().rstrip().split()))

        if (n1==g and n2==h) or (n1==h and n2==g): wei = wei+0.0001

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

    dijkStart = dijkstra(s)
    
    answers=[]
    for i in goals:
        if str(type(dijkStart[i]))=="<class 'float'>":
            answers.append(str(i))
    answers.sort()
    ansList.append(answers)


#printing out answers
for answers in ansList:
    print(" ".join(answers))