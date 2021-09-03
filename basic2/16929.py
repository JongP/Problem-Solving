import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
graph=[]

for _ in range(n):
    graph.append(input().rstrip())    


visited = [[0]*m for _ in range(n)]


def DFS(i,j,depth):
    char = graph[i][j]

    if i>0 and  graph[i-1][j]==char:
        if visited[i-1][j]==0:
            visited[i-1][j]=depth+1
            DFS(i-1,j,depth+1)
        elif depth-visited[i-1][j]>2:
            print("Yes")
            sys.exit()
    if j>0 and  graph[i][j-1]==char:
        if visited[i][j-1]==0:
            visited[i][j-1]=depth+1
            DFS(i,j-1,depth+1)
        elif depth-visited[i][j-1]>2:
            print("Yes")
            sys.exit()
    if i<n-1 and  graph[i+1][j]==char:
        if visited[i+1][j]==0:
            visited[i+1][j]=depth+1
            DFS(i+1,j,depth+1)
        elif depth-visited[i+1][j]>2:
            print("Yes")
            sys.exit()
    if j<m-1 and  graph[i][j+1]==char:
        if visited[i][j+1]==0:
            visited[i][j+1]=depth+1
            DFS(i,j+1,depth+1)
        elif depth-visited[i][j+1]>2:
            print("Yes")
            sys.exit()

for i in range(n):
    for j in range(m):
        if visited[i][j]!=0: continue
        visited[i][j]=1
        DFS(i,j,1)
print("No")