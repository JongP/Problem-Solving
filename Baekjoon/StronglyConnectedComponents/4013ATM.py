#I absolutely failed to reduce memory
#I'd like to take optimap solution of SCC 
#https://www.acmicpc.net/source/25583408
import sys
from collections import deque

sys.setrecursionlimit(10**9)

def tarjan_dfs(node):
    global cnt, scc_cnt
    cnt += 1
    dfsn[node] = cnt
    stack.append(node)
    
    result = dfsn[node]
    for i in graph[node]:
        if dfsn[i] == 0:
            result = min(result, tarjan_dfs(i))
        elif not finished[i]:
            result = min(result, dfsn[i])

    if result == dfsn[node]:
        current_scc = []
        while True:
            t = stack.pop()
            finished[t] = True
            current_scc.append(t)
            scc_num[t] = scc_cnt
            if t == node:
                break
        scc_lst.append(current_scc)
        scc_cnt += 1
    
    return result

def topology_sort(q):
    while q:
        node = q.popleft()
        for i in scc_adj[node]:
            if isTrue_from_start_to_scc[node]:
                scc_max[i] = max(scc_max[i], scc_max[node]+scc_cash[i])
                isTrue_from_start_to_scc[i] = True
            scc_outd[i] -= 1
            if scc_outd[i] == 0:
                q.append(i)

n, m = map(int, sys.stdin.readline().split())

# ---make SCC-----------------------------------------
graph = [[] for _ in range(n+1)]
dfsn = [0 for _ in range(n+1)]; cnt = 0
finished = [False for _ in range(n+1)]
scc_num = [0 for _ in range(n+1)]
scc_lst = []
stack = []
scc_cnt = 0

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)

for i in range(1, n+1):
    if dfsn[i] == 0:
        tarjan_dfs(i)
# ---make SCC end-----------------------------------------

# ---check SCC----------------------------------------
cash = [0]
for i in range(n):
    cash.append(int(sys.stdin.readline()))

s, p = map(int, sys.stdin.readline().split())

has_rest = [False for _ in range(n+1)]
r = list(map(int, sys.stdin.readline().split()))
for i in r:
    has_rest[i] = True

scc_adj = [[] for _ in range(n+1)]
scc_start = 0
scc_cash = [0 for _ in range(n+1)]
scc_outd = [0 for _ in range(n+1)]
scc_has_rest = [False for _ in range(n+1)]

for i in range(1, n+1):
    scc_i = scc_num[i]
    scc_cash[scc_i] += cash[i]
    if has_rest[i]:
        scc_has_rest[scc_i] = True
    if i == s:
        scc_start = scc_i

    for j in graph[i]:
        scc_j = scc_num[j]
        if scc_i == scc_j:
            continue
        scc_adj[scc_i].append(scc_j)
        scc_outd[scc_j] += 1
# ---check SCC end----------------------------------------

# ---sort SCC-----------------------------------------
scc_max = [0 for _ in range(n+1)]
isTrue_from_start_to_scc = [False for _ in range(n+1)]

q = deque()
for i in range(scc_cnt):
    scc_max[i] = scc_cash[i]
    if i == scc_start:
        isTrue_from_start_to_scc[i] = True
    if scc_outd[i] == 0:
        q.append(i)

topology_sort(q)
# ---sort SCC end-----------------------------------------

res = 0
for i in range(scc_cnt):
    if scc_has_rest[i] and isTrue_from_start_to_scc[i]:
        res = max(res, scc_max[i])

print(res)

#https://www.acmicpc.net/source/37201773

import sys
I=sys.stdin.readline
sys.setrecursionlimit(10**7)

#Inputs
v,e=map(int,I().split())
graph=[[] for _ in range(v+1)]
money=[0]
for _ in range(e):
    a,b=map(int,I().split())
    graph[a].append(b)
for _ in range(v):
    money.append(int(I()))
start_node,p=map(int,I().split())
r=list(map(int,I().split()))

#SCC 구하기(Tarjan's Algorithm)
global id,scc_num
id=0
scc_num=0
visited=[0]*(v+1) #i번 정점을 방문했는지 여부
finished=[0]*(v+1) #i번 정점의 dfs가 끝났는지 여부 / dfs가 끝나면 i가 포함된 SCC의 index 저장
s=[] #dfs를 돌면서 node를 저장할 스택
SCC_money=[0] #각 SCC에 포함된 돈의 총 합
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
        scc_num+=1
        scc_money=0
        while True: 
            t=s.pop()
            scc_money+=money[t]
            finished[t]=scc_num
            if t==x:
                break
        SCC_money.append(scc_money)
    return parent

for i in range(1,v+1):
    if not visited[i]: dfs(i)

#SCC끼리의 방향그래프 만들기
SCC_graph=[set([]) for _ in range(scc_num+1)]
for i in range(1,v+1):
    scc_num_i=finished[i]
    for x in graph[i]:
        if finished[x]!=scc_num_i:
            SCC_graph[scc_num_i].add(finished[x])

start_scc=finished[start_node]
dp=[0]*(scc_num+1)
dp[start_scc]=SCC_money[start_scc]
for i in range(start_scc,0,-1):
    for next in SCC_graph[i]:
        dp[next]=max(dp[next],dp[i]+SCC_money[next])
ans=0
for rest in r:
    ans=max(ans,dp[finished[rest]])
print(ans)




#unsolved own solution
import sys
input=lambda : sys.stdin.readline().rstrip()

sys.setrecursionlimit(250000)

N,M=map(int,input().split())
graph=[[] for _ in range(N)]


for _ in range(M):
    a,b=map(lambda x: int(x)-1,input().split())
    graph[a].append(b)

moneys=[int(input()) for _ in range(N)]

S,P=map(int,input().split());S-=1

restaurants=set(map(lambda x:int(x)-1,input().split()))


#SCC
id=0
sn=-1
dfsn=[-1]*N
sccNums=[-1]*N
sccSums=[]

sccRes=set()
stk=[]

def dfs(node):
    global id,sn
    dfsn[node]=id;id+=1
    stk.append(node)


    res=dfsn[node]
    for nextt in graph[node]:
        if dfsn[nextt]==-1:
            res=min(res,dfs(nextt))
        elif dfsn[nextt]!=-2:
            res=min(res,dfsn[nextt])
    
    if dfsn[node]==res:
        sn+=1
        sccSum=0
        while True:
            tmp=stk.pop()
            sccNums[tmp]=sn
            sccSum+=moneys[tmp]
            dfsn[tmp]=-2#if we don't have this


            if tmp==node:
                break
        sccSums.append(sccSum)

    return res

for i in range(N):
    if dfsn[i]==-1:
        dfs(i)

#build graph for  topological sorting
sccGraph=[set() for _ in range(sn+1)]
sccS=sccNums[S]
inDegrees=[0]*(sn+1)


for i in range(N):
        if i in restaurants:
            sccRes.add(sccNums[i])
        for nextt in graph[i]:
            if sccNums[i]!=sccNums[nextt] and sccNums[nextt] not in sccGraph[sccNums[i]]:
                sccGraph[sccNums[i]].add(sccNums[nextt])
                inDegrees[sccNums[nextt]]+=1



#topological sorting
resL=[0]*(sn+1)
reachable=[False]*(sn+1)
reachable[sccS]=True
stk=[]
for i in range(sn+1):
    if inDegrees[i]==0:
        stk.append(i)

while stk:
    cur=stk.pop()

    resL[cur]+=sccSums[cur]

    for nextt in sccGraph[cur]:
        inDegrees[nextt]-=1
        if inDegrees[nextt]==0:
            stk.append(nextt)

        if reachable[cur]:
            reachable[nextt]=True
            resL[nextt]=max(resL[nextt],resL[cur])

res=0
for r in sccRes:
    res=max(res,resL[r])

print(res)
