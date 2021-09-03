import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

graph = {}

for _ in range(m):
    a,b = map(int,input().rstrip().split())
    if a not in graph:
        graph[a]=[b]
    else:
        graph[a].append(b)

    if b not in graph:
        graph[b]=[a]
    else:
        graph[b].append(a)


def DFS(node,depth):

    if depth==4:
        print(1)
        sys.exit()

    if node not in graph:
        return
    
    for next in graph[node]:
        if visited[next]==0:
            visited[next]=1
            DFS(next,depth+1)
            visited[next]=0
               

answer=0
for i in range(n):
    visited =[0]*n
    visited[i]=1
    DFS(i,0)
print(0)