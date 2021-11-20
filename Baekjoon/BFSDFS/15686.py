from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline


def chickenLength(house):

    queue = deque([house])
    visited = [[0]*(n+1) for _ in range(n+1)]
    visited[house[0]][house[1]]=1
    count=1


    while queue:
        l = len(queue)

        for _ in range(l):
            x,y = queue.popleft()

            if x>1:
                if graph[x-1][y]==2:
                    return count
                elif  visited[x-1][y]==0:
                    visited[x-1][y]=1
                    queue.append((x-1,y))
            if x<n:
                if graph[x+1][y]==2:
                    return count
                elif visited[x+1][y]==0:
                    visited[x+1][y]=1
                    queue.append((x+1,y))
            if y>1:
                if graph[x][y-1]==2:
                    return count
                elif visited[x][y-1]==0:
                    visited[x][y-1]=1
                    queue.append((x,y-1))
            if y<n:
                if graph[x][y+1]==2:
                    return count
                elif visited[x][y+1]==0:
                    visited[x][y+1]=1
                    queue.append((x,y+1))
        count+=1
    return count

n,m= map(int, input().rstrip().split())

graph = [[0]*(n+1)]

houses=[]
chickens =[]
for i in range(n):
    row = list(map(int,input().rstrip().split()))
    for j in range(n):
        if row[j]==1:
            houses.append((i+1,j+1))
        elif row[j]==2:
            chickens.append((i+1,j+1))
    graph.append([0]+row)


num_chickens = len(chickens)
minNum=int(1e9)
for comb in combinations(chickens,num_chickens-m):
    for x,y in comb:
        graph[x][y]=1

    tmpLength=0
    for house in houses:
        tmpLength+= chickenLength(house)
    
    if minNum>tmpLength: minNum = tmpLength
    #print(comb, tmpLength)

    for x,y in comb:
        graph[x][y]=2


print(minNum)