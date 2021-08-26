import heapq
import sys
ip=sys.stdin.readline

n,e = tuple(map(int,ip().rstrip().split()))
graph={}

for _ in range(e):
    n1,n2, wei = tuple(map(int,ip().rstrip().split()))

    if n1 not in graph:
        graph[n1]=[(wei,n2)]
    else:
        graph[n1].append((wei,n2))

    if n2 not in graph:
        graph[n2]=[(wei,n1)]
    else:
        graph[n2].append((wei,n1))

n1,n2 = tuple(map(int,ip().rstrip().split()))

#find shotrtest length from start to n1 and n2
def fromAtoBC(start,n1,n2):
    heap=[]
    distances=[sys.maxsize]*(n+1)
    distances[start]=0
    node_set=set()

    heapq.heappush(heap,(0,start))

    while (n1 not in node_set or n2 not in node_set) and heap:
        _,node = heapq.heappop(heap)
        if node in node_set:
            continue

        node_set.add(node)

        if node not in graph: continue

        for iter_w,iter_n in graph[node]:
            if iter_n in node_set: continue
            if distances[node]+iter_w < distances[iter_n]:
                distances[iter_n] = distances[node] +iter_w
                heapq.heappush(heap,(distances[iter_n],iter_n))

    return (distances[n1],distances[n2])

def fromAtoB(start,end):
    heap=[]
    distances=[sys.maxsize]*(n+1)
    distances[start]=0
    node_set=set()

    heapq.heappush(heap,(0,start))

    while end not in node_set and heap:
        _,node = heapq.heappop(heap)
        if node in node_set:
            continue

        node_set.add(node)

        if node not in graph: continue

        for iter_w,iter_n in graph[node]:
            if iter_n in node_set: continue
            if distances[node]+iter_w < distances[iter_n]:
                distances[iter_n] = distances[node] +iter_w
                heapq.heappush(heap,(distances[iter_n],iter_n))

    return (distances[end])


route1a, route2a = fromAtoBC(1,n1,n2)

if route1a == sys.maxsize or route2a==sys.maxsize:
    print(-1)
else:

    routeCommon = fromAtoB(n1,n2)
    route2b, route1b = fromAtoBC(n,n1,n2)
    if routeCommon==sys.maxsize or route1b==sys.maxsize or route2b==sys.maxsize:
        print(-1)
    elif route1a+route1b>route2a+route2b:
        print(route2a+route2b+routeCommon)
    else:
        print(route1a+route1b+routeCommon)