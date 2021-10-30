#https://programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque

def isConnected(str1,str2):
    cnt=False
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            if(cnt==True):
                return False
            cnt=True
    return True;

def solution(begin, target, words):
    answer = 1
    canGo=False
    #["hot", "dot", "dog", "lot", "log", "cog"]	["begin"]
    l=len(words)
    visited=[0]*(l+1)
    graph=[[0]*(l+1) for _ in range(l+1)]
    for i in range(l):
        if isConnected(words[i],begin):
            if(words[i]==begin):
                graph[i][l]=0
                graph[l][i]=0
            else:
                graph[i][l]=1
                graph[l][i]=1
        if not canGo and words[i]==target:
            target=i
            canGo=True

        for j in range(i+1,l):
            if isConnected(words[i],words[j]):
                graph[i][j]=1
                graph[j][i]=1
    if not canGo:
        return 0
    

    queue=deque([l])
    visited[l]=1
    while queue:
        qLen=len(queue)
        for _ in range(qLen):
            cur=queue.popleft()
            for i in range(l):
                if graph[cur][i]==1 and visited[i]==0:
                    if i==target:
                        return answer
                    visited[i]=1
                    queue.append(i)
        print(visited,answer)    


        answer+=1


    return answer
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))