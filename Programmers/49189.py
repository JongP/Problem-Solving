#가장 먼 노드 
#https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    answer = 0

    visited=[0]*(n+1)
    graph={}


    #building graph
    for a,b in edge:
        if a not in graph:
            graph[a]=[b]
        else:
            graph[a].append(b)

        if b not in graph:
            graph[b]=[a]
        else:
            graph[b].append(a)

    visited[1]=1
    queue=deque([1])

    while queue:
        l=len(queue)
        tmp=0
        for _ in range(l):
            cur = queue.popleft()

            if cur not in graph:
                continue

            for node in graph[cur]:
                if visited[node]==0:
                    visited[node]=1
                    tmp+=1
                    queue.append(node)
        if(tmp!=0):
            answer=tmp
    print(answer)
    return answer


solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])