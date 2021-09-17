import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def BFS(graph,locations):

    queue = deque(locations)

    while queue:
        x,y = queue.popleft()

        graph[x][y]=2

        if x>0 and graph[x-1][y]==0:
            graph[x-1][y]=2
            queue.append((x-1,y))
        if x<n-1 and graph[x+1][y]==0:
            graph[x+1][y]=2
            queue.append((x+1,y))
        if y>0 and graph[x][y-1]==0:
            graph[x][y-1]=2
            queue.append((x,y-1))
        if y<m-1 and graph[x][y+1]==0:
            graph[x][y+1]=2
            queue.append((x,y+1))

def count_safe(graph):
    count=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0: 
                count+=1
    return count


n,m = map(int,input().rstrip().split())

graph=[]
land=[]
virus=[]
for i in range(n):
    row =list(map(int,input().rstrip().split()))
    for j in range(m):
        if row[j]==0:
            land.append((i,j))
        elif row[j]==2:
            virus.append((i,j))
    graph.append(row)

maxNum=0
for comb in combinations(land,3):
    temp_graph =[]
    for row in graph : 
        temp_graph.append(row[:])
    
    for x,y in comb:
        temp_graph[x][y]=1

    BFS(temp_graph,virus)
    num=count_safe(temp_graph)
    if num>maxNum: maxNum=num

print(maxNum)
