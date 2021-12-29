from collections import defaultdict
import sys
input=sys.stdin.readline
#map(int,input().rstrip().split())
sys.setrecursionlimit(10**5)

n=int(input())
graph=defaultdict(list)

visited=[0]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node,parent):
    visited[node]=parent

    for nxt in graph[node]:
        if visited[nxt]==0:
            dfs(nxt,node)

dfs(1,-1)

[print(elem) for elem in visited[2:]]