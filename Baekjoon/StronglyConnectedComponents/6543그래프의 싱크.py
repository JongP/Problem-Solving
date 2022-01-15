import sys
input=lambda : sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**5)

def getGraph(n,m):
    line=list(map(int,input().split()))
    graph=[[] for _ in range(n)]
    for i in range(m):
        a,b=line[2*i:2*i+2]
        graph[a-1].append(b-1)
    return graph

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
            tmpL.append(t+1)
            sccNums[t]=sn
            dfsn[t]=-2
            if t==node:
                break
        sn+=1
        sccL.append(tmpL)
    
    return parent



line=list(map(int,input().split()))

while len(line)==2:
    N,M=line

    graph=getGraph(N,M)

    id=sn=0
    dfsn=[-1]*N
    sccNums=[-1]*N
    stk=[]
    sccL=[]
    for i in range(N):
        if dfsn[i]==-1:
            dfs(i)

    noOuts=[True]*(sn)
    for i in range(N):
        for j in graph[i]:
            if sccNums[i]!=sccNums[j]:
                noOuts[sccNums[i]]=False

    res=[]
    for i in range(sn):
        if noOuts[i]:
            res.extend(sccL[i])

    res.sort()
    print(*res)


    line=list(map(int,input().split()))





#https://www.acmicpc.net/source/35889540

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)

while True:
    arr = list(map(int, read().split()))
    if 1 == len(arr):
        break
    n, m = arr
    arr = list(map(int, read().split()))
    edges = [arr[i:i+2] for i in range(0, 2*m, 2)]
    graph = [[] for _ in range(n+1)]
    for a, b in edges:
        graph[a].append(b)

    disc = [0] * (n+1)  # discovered
    low = [0] * (n+1)  # lowest
    finished = [False] * (n+1)  # finished if included in SCC
    st = []  # stack for making SCC
    scc = []
    ans = 0
    result = set()

    def dfs(cur,):
        global ans, t, result
        disc[cur] = low[cur] = t
        st.append(cur)
        t += 1

        for nxt in graph[cur]:
            if not disc[nxt]:  # tree edge
                dfs(nxt)
                low[cur] = min(low[cur], low[nxt])
            elif not finished[nxt]:  # backward edge (elif) & not cross edge (not finished)
                low[cur] = min(low[cur], disc[nxt])

        if low[cur] == disc[cur]:
            local_scc = set()
            while True:
                top = st.pop()
                finished[top] = True
                local_scc.add(top)
                if top == cur:
                    break

            has_outgoing = False
            for e in local_scc:
                for nxt in graph[e]:
                    if nxt not in local_scc:
                        has_outgoing = True
                        break
            if not has_outgoing:
                result |= local_scc


    for i in range(1, n+1):
        if not disc[i]:
            t = 1
            dfs(i,)

    print(*sorted(result))