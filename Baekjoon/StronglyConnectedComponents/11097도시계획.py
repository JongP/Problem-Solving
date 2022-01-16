#tiny? hint
import sys
input=lambda : sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**5)


def dfs(node):
    global id,sn
    dfsn[node]=id
    id+=1
    stk.append(node)

    parent=dfsn[node]
    for nextt in graph[node]:
        if dfsn[nextt]==-1:
            parent=min(parent,dfs(nextt))
        elif dfsn[nextt]!=-2:
            parent=min(parent,dfsn[nextt])

    if dfsn[node]==parent:
        tmpL=[]
        while True:
            t=stk.pop()
            dfsn[t]=-2
            sccNums[t]=sn
            tmpL.append(t)
            if t==node:
                break
        sccL.append(tmpL)
        sn+=1

    return parent



for i in range(int(input())):
    if i!=0:
        print()

    input()
    n=int(input())
    graph=[[] for _ in range(n)]
    for i in range(n):
        line=input()
        for j in range(n):
            if line[j]=="1" and i!=j:
                graph[i].append(j)
    

    #build scc
    id=sn=0
    dfsn=[-1]*n
    sccL=[]
    sccNums=[-1]*n
    stk=[]

    for i in range(n):
        if dfsn[i]==-1:
            dfs(i)

    #build sccGraph
    sccGraph=[set() for _ in range(sn)]


    for i in range(n):
        sccS=sccNums[i]

        for j in graph[i]:
            sccE=sccNums[j]
            if sccS!=sccE and sccE not in sccGraph[sccS]:  
                sccGraph[sccS].add(sccE)


    
    for i in range(sn):
        tmp=sccGraph[i].copy()
        for nextt in sccGraph[i]:
            tmp-=sccGraph[nextt]
        sccGraph[i]=tmp

    extraNum=0
    extraRoads=[]
    for i in range(sn):
        extraNum+=len(sccGraph[i])
        for nextt in sccGraph[i]:
            extraRoads.append((sccL[i][0],sccL[nextt][0]  ))

    #result
    resNum=extraNum
    for scc in sccL:
        resNum+=len(scc) if len(scc)>1 else 0
    print(resNum)

    for scc in sccL:
        for i in range(len(scc)-1):
            print(scc[i]+1,scc[i+1]+1)
        if len(scc)>1:
            print(scc[-1]+1,scc[0]+1)

    for a,b in extraRoads:
        print(a+1,b+1)
