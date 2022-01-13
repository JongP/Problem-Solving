import sys
from collections import defaultdict
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())




ansL=[]


for _ in range(int(input())):
    n=int(input())
    ranks=list(map(lambda x: int(x)-1,input().split()))

    graph=defaultdict(set)
    inDegrees=[0]*n

    #last year's graph
    for i in range(n):
        for j in range(i+1,n):
            graph[ranks[i]].add(ranks[j])
        inDegrees[ranks[i]]=i

    
    #this years' graph
    for _ in range(int(input())):
        a,b=map(lambda x :int(x)-1,input().split())

        if a in graph[b]:
            a,b=b,a

        graph[a].remove(b)
        graph[b].add(a)
        inDegrees[b]-=1
        inDegrees[a]+=1
    
    que=[]
    res=[]
    for i in range(n):
        if inDegrees[i]==0:
            que.append(i)
    flag=False
    while que:
        if len(que)>1:
            ansL.append("?")
            flag=True
            break
        cur=que.pop()
        res.append(str(cur+1))
        for nextt in graph[cur]:
            inDegrees[nextt]-=1
            if inDegrees[nextt]==0:
                que.append(nextt)

    if flag:
        continue
    elif len(res)!=n:
        ansL.append(None)    
    else:
        ansL.append(res)



[print(" ".join(a) if a else "IMPOSSIBLE") for a in ansL]