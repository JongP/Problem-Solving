#순위
#https://programmers.co.kr/learn/courses/30/lessons/49191
from collections import deque

def solution(n, results):
    answer = 0

    table=[[0]*(n+1) for _ in range(n+1)]

    for a,b in results:
        table[a][b]=1
        table[b][a]=-1


    for cur in range(1,n+1):
        queue=deque([cur])
        visited=[0]*(n+1)
        visited[cur]=1

        #num of winners
        numWinner=0
        while queue:
            node=queue.popleft()
            for i in range(1,n+1):
                if table[node][i]==1 and visited[i]==0:
                    visited[i]=1
                    queue.append(i)
                    numWinner+=1
                



        #num of losers
        numLosers=0
        queue=deque([cur])
        visited=[0]*(n+1)
        visited[cur]=1
        while queue:
            node=queue.popleft()
            for i in range(1,n+1):
                if table[node][i]==-1 and visited[i]==0:
                    visited[i]=1
                    queue.append(i)
                    numLosers+=1

        if numLosers+numWinner+1==n:
            answer+=1

    print(answer)
    return answer


solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])