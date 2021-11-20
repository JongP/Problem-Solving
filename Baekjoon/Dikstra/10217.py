#https://www.acmicpc.net/board/view/27652
from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

t = int(input())

ansList=[]

for _ in range(t):
    n,m,k = map(int,input().rstrip().split())
    graph={}
    answer=INF

    visited=[[0]*(m+1) for _ in range(n+1)]
    dists=[[INF]*(m+1) for _ in range(n+1)]

    #building graph
    for _ in range(k):
        u,v,c,d = map(int,input().rstrip().split())

        if u not in graph:
            graph[u]={v:[(c,d)]}
        elif v not in graph[u]:
            graph[u][v] = [(c,d)]
        else:
            graph[u][v].append((c,d))


    dists[1][0]=0
    visited[1][0]=1
    queue=deque([(1,0,0)]) #[(node,cost)...]

    while queue:
        node,cost,dist = queue.popleft()
        
        if dist>dists[node][cost]: continue
        if node not in graph: continue

        for next_node in graph[node]:
            for next_cost,next_dist in graph[node][next_node]:
                new_dist = dist + next_dist
                new_cost = cost + next_cost

                if new_cost>m: continue

                if  dists[next_node][new_cost] > new_dist:
                    dists[next_node][new_cost] = new_dist
                    visited[next_node][new_cost]=1
                    queue.append((next_node,new_cost,new_dist))

    for i in range(m+1):
        if visited[n][i] and dists[n][i]<answer:
            answer=dists[n][i]

    if answer==INF:
        answer="Poor KCM"        

    ansList.append(answer)

#printing out answer
for answer in ansList:
    print(answer)