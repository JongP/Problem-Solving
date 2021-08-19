#https://mattlee.tistory.com/50
import sys
import heapq
input= sys.stdin.readline

v,e = tuple(map(int,input().rstrip().split()))
start = int(input())

graph = {}
distances = [sys.maxsize]*(v+1)
distances[start]=0
queue=[(0,start)]#n(node,length)
node_set = set()


#creating graph
for _ in range(e):
    u,v,w = tuple(map(int,input().rstrip().split()))
    if u not in graph:
        graph[u]={v:w}
    elif v not in graph[u]:
        graph[u][v]=w
    elif graph[u][v]>w:
        graph[u][v]=w



while queue:
    length, node = heapq.heappop(queue)
    if node not in node_set:
        node_set.add(node)
    else:
        continue

    if node in graph:
        for iter_n, iter_w in graph[node].items():
            if iter_n in node_set: continue
            if length+iter_w < distances[iter_n]:
                heapq.heappush(queue,(length+iter_w,iter_n))
                distances[iter_n]=length+iter_w

distances=distances[1:]
for i in distances:
    if i == sys.maxsize:
        print("INF")
    else:
        print(i)