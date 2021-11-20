#https://velog.io/@younge/Python-최단-경로-벨만-포드Bellman-Ford-알고리즘
import sys
input = sys.stdin.readline
INF=int(1e9)

n,m = tuple(map(int,input().rstrip().split()))
graph = {}

for _ in range(m):
    a,b,c = tuple(map(int,input().rstrip().split()))

    if a not in graph:
        graph[a]= {b:c}
    elif b in graph[a]:
        if c<graph[a][b]: graph[a][b]=c
    else: 
        graph[a][b]=c

def bf(start):
    dist=[INF]*(n+1)
    dist[start]=0

    for _ in range(n-1):
        for node in graph:
            if dist[node]==INF: continue
            for next_node in graph[node]:
                if dist[next_node] > dist[node]+graph[node][next_node]:
                    dist[next_node]= dist[node]+graph[node][next_node]

    for node in graph:
        if dist[node]==INF: continue
        for next_node in graph[node]:
            if dist[next_node] > dist[node]+graph[node][next_node]:
                return [-1]

    return dist[2:]

dist=bf(1)
#print(dist)
for i in dist:
    if i==INF: i =-1
    print(i)