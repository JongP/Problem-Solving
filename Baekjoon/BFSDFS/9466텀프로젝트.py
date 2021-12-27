import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
t=int(input())
ans=[]

def goDFS(graph,visited,n,i):
    global res
    visited[i]=1

    nxt=graph[i]
    if visited[nxt]==1:
        while nxt!=i:
            nxt=graph[nxt]
            res-=1
        res-=1
    elif visited[nxt]==0:
        goDFS(graph,visited,n,nxt)
    
    visited[i]=2


for _ in range(t):
    n=int(input())
    graph= list(map(int,input().rstrip().split()))
    graph=[x-1 for x in graph]
    visited=[0]*n

    res=n
    #print(graph)

    for i in range(n):
        if visited[i]==0:
            goDFS(graph,visited,n,i)
    
    ans.append(res)
    



[print(a) for a in ans]