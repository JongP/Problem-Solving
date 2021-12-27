import sys
input=sys.stdin.readline

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))



def goDFS(parent,idx):
    visited[idx]=1

    for i in range(n):
        if graph[idx][i]==1 and visited[i]==0:
            graph[parent][i]=1
            goDFS(parent,i)
    if parent!=idx and graph[idx][parent]==1:
        graph[parent][parent]=1
        
        

for i in range(n):
    visited=[0]*n
    if visited[i]==0:
        goDFS(i,i)



[print(" ".join(map(str,line))) for line in graph]