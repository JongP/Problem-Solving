import sys
from collections import defaultdict
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())

ansL=[]

for _ in range(int(input())):
    K,M,P=map(int,input().split())

    graph=defaultdict(list)
    inDegrees=[0]*M
    maxIn=[0]*M
    res=[1]*M
    
    for _ in range(P):
        A,B=map(lambda x:int(x)-1,input().split())
        inDegrees[B]+=1
        graph[A].append(B)

    que=[]

    for i in range(M):
        if inDegrees[i]==0:
            que.append(i)

    while que:
        cur=que.pop()

        for nextt in graph[cur]:
            inDegrees[nextt]-=1
            if inDegrees[nextt]==0:
                que.append(nextt)
            
            if maxIn[nextt]<res[cur]:
                maxIn[nextt]=res[cur]
                res[nextt]=res[cur]
            elif maxIn[nextt]==res[cur]:
                res[nextt]=res[cur]+1
            
    ansL.append((K,res[-1]))





[print(ansL[i][0],ansL[i][1])  for i in range(len(ansL))]