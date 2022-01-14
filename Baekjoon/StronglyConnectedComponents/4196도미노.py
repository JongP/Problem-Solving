import sys
input=lambda : sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**5)

ansL=[]


def dfs(node):
    global id,sn
    dfsn[node]=id
    id+=1
    stk.append(node)

    res=dfsn[node]
    for nextt in graph[node]:
        if dfsn[nextt]==-1:
            res=min(res,dfs(nextt))
        elif finished[nextt]==0:
            res=min(res,dfsn[nextt])

    
    if dfsn[node]==res:
        sn+=1
        while True:
            tmp=stk.pop()
            sNums[tmp]=sn
            finished[tmp]=True
            if tmp==node:
                break

    return res #don't forget
        


for _ in range(int(input())):
    N,M=map(int,input().split())
    graph=[[] for _ in range(N)]

    #build map
    for _ in range(M):
        a,b=map(lambda x : int(x)-1,input().split())
        graph[a].append(b)

    dfsn=[-1]*N
    sNums=[-1]*N
    finished=[0]*N
    stk=[]
    id=sn=0
    
    for i in range(N):
        if dfsn[i]==-1:
            dfs(i)

    inDegrees=[1]*sn

    for i in range(N):
        for j in graph[i]:
            if sNums[i]!=sNums[j]:
                inDegrees[sNums[j]]=0

    ansL.append(sum(inDegrees))


[print(ans) for ans in ansL]