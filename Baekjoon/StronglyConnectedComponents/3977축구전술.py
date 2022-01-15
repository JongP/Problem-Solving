import sys
input=lambda : sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**6)


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


ansL=[]
t=int(input())
for tt in range(t):
    if tt!=0:
        print("")
    #graph building
    if tt!=0:
        input()
    N,M=map(int,input().split())
    graph=[[ ] for _ in range(N)]
    for _ in range(M):
        a,b=map(int,input().split())
        graph[a].append(b)

    #buildign scc O(V+E)
    id=sn=0
    dfsn=[-1]*N
    sccL=[]
    sccNums=[-1]*N
    stk=[]
    for i in range(N):
        if dfsn[i]==-1:
            dfs(i)


    #scc graph building O(V+E)
    sccGraph=[[] for _ in range(sn)]
    vis=set([i for i in range(sn)])
    for i in range(N):
        for j in graph[i]:
            if sccNums[i]!=sccNums[j]:
                sccGraph[sccNums[i]].append(sccNums[j])
                vis.discard(sccNums[j])
            

    if len(vis)==1:
        start=vis.pop()
        sccL[start].sort()
        [print(a) for a in sccL[start]]
    else:
        print("Confused")
    


#https://www.acmicpc.net/source/37178946
import sys
I=sys.stdin.readline
sys.setrecursionlimit(10**7)

def solve():
    v,e=map(int,I().split())
    graph=[[] for _ in range(v)]
    for _ in range(e):
        a,b=map(int,I().split())
        graph[a].append(b)

    global id,scc_num  
    id=0
    scc_num=0
    visited=[0]*v
    finished=[0]*v
    s=[]
    SCC=[0]
    def dfs(x):
        global id,scc_num
        id+=1
        visited[x]=id
        parent=id
        s.append(x)
        for y in graph[x]:
            if not visited[y]:
                parent=min(parent,dfs(y))
            elif not finished[y]:
                parent=min(parent,visited[y])
        
        if parent==visited[x]:
            scc=[]
            scc_num+=1
            while True: 
                t=s.pop()
                scc.append(t)
                finished[t]=scc_num
                if t==x: break
            SCC.append(scc)
        return parent

    for i in range(v):
        if not visited[i]: dfs(i)
    
    SCC_indegree=[0]*(scc_num+1)
    for i in range(v):
        scc_num_i=finished[i]
        for x in graph[i]:
            if finished[x]!=scc_num_i:
                SCC_indegree[finished[x]]+=1
    if sum([x==0 for x in SCC_indegree[1:]])>1:
        print('Confused')
        return
    start=SCC_indegree[1:].index(0)+1
    print(*sorted(SCC[start]),sep='\n')

t=int(I())
solve()
for _ in range(t-1):
    I()
    print()
    solve()


