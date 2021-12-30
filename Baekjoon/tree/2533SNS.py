#recursion takes too much time. u can use stack if u can

from collections import defaultdict
import sys
input=sys.stdin.readline
#map(int,input().rstrip().split())
sys.setrecursionlimit(10**6)

graph=defaultdict(list)
n=int(input())
visited=[0]*n
for _ in range(n-1):
    a,b=map(int,input().rstrip().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)



def traverse(node):
    visited[node]=1
    flag=False

    resL=[]
    for child in graph[node]:
        if visited[child]==1:
            continue
        resL.append(traverse(child))
    
    if len(resL)==0:
        return (1,0)

    res1=1
    res2=0
    minGap=int(2e9)

    for r1,r2 in resL:
        res1+=min(r1,r2)
        res2+=r1

    return res1,res2
print(min(traverse(0)))



#https://www.acmicpc.net/source/33404244
from sys import stdin
from collections import deque

def main():
    global graph, cache
    N = int(stdin.readline())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        v1, v2 = map(int, stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    DP = [[0, 1] for _ in range(N + 1)]
    DP[0][1] = 0
    parent = [-1] * (N + 1)
    parent[1] = 0
    queue = deque()
    queue.append(1)
    stack = deque()
    stack.append(1)
    while queue:
        v = queue.popleft()
        for _v in graph[v]:
            if parent[_v] != -1:
                continue
            parent[_v] = v
            queue.append(_v)
            stack.append(_v)
    while stack:
        v = stack.pop()
        p = parent[v]
        DP[p][0] += DP[v][1]
        DP[p][1] += min(DP[v][1], DP[v][0])
    print(min(DP[0]))

main()

