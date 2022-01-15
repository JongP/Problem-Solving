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
        sccSum=0
        while True:
            t=stk.pop()
            sccNums[t]=sn
            dfsn[t]=-2
            sccSum+=1

            if t==node:
                break
        sccSums.append(sccSum)
        sn+=1

    return parent

N,M,S,T=map(int,input().split())
S-=1;T-=1

graph=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(lambda x:int(x)-1, input().split())
    graph[a].append(b)


dfsn=[-1]*N
sccNums=[-1]*N
sccSums=[]
stk=[]
id=sn=0


for i in range(N):
    if dfsn[i]==-1:
        dfs(i)

sccS=sccNums[S]
sccT=sccNums[T]

#sccGraph
sccGraph=[set() for _ in range(sn)]
inDegrees=[0]*sn
reachable=[False]*sn
reachable[sccS]=True
maxSum=[0]*sn
maxSum[sccS]=sccSums[sccS]

for i in range(N):

    for j in graph[i]:
        if sccNums[i]!=sccNums[j] and sccNums[j] not in sccGraph[sccNums[i]]:
            sccGraph[sccNums[i]].add(sccNums[j])
            inDegrees[sccNums[j]]+=1


stk=[]

for i in range(sn):
    if inDegrees[i]==0:
        stk.append(i)

while stk:
    cur=stk.pop()

    for nextt in sccGraph[cur]:
        inDegrees[nextt]-=1
        if inDegrees[nextt]==0:
            stk.append(nextt)
        if reachable[cur]:
            reachable[nextt]=True
            maxSum[nextt]=max(maxSum[nextt],maxSum[cur]+sccSums[nextt])

#print(sn)
#print(sccSums)
print(maxSum[sccT])


#https://www.acmicpc.net/source/26017458
input = __import__('sys').stdin.readline
import sys
from _collections import deque
sys.setrecursionlimit(100000000)

def SCC(adj):
    #n = len(adj)-1
    S = []
    SCCs = [0]*(n+1)
    SCCn = []
    pre = [0]*(n+1)
    post = [0]*(n+1)
    def dfs(u):
        global c, cnt
        c+=1
        pre[u]=c
        S.append(u)
        minpre = pre[u]
        for v in adj[u]:
            if not pre[v]: minpre = min(minpre, dfs(v))
            elif not post[v]: minpre = min(minpre, pre[v])
        if minpre == pre[u]:
            cnt+=1
            SCCn.append(0)
            while True:
                v = S.pop()
                SCCs[v]=cnt
                SCCn[-1]+=1
                post[v]=1
                if v==u: break
        return minpre

    for i in range(1,n+1):
        if not pre[i]: dfs(i)

    return SCCs, SCCn

c=0
cnt = -1
n,m,s,e = map(int,input().split())
adj = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)

S = [s]
visit = [False]*(n+1)
while S:
    if visit[e]: break
    u = S.pop()
    for v in adj[u]:
        if not visit[v]:
            visit[v]=True
            S.append(v)
if not visit[e]: print(0); sys.exit()

SCCs, SCCn = SCC(adj)

aadj = [set() for i in range(cnt+2)]
for u in range(1,n+1):
    Su = SCCs[u]
    for v in adj[u]:
        Sv = SCCs[v]
        if Su != Sv: aadj[Su].add(Sv)
dp = [0]*(cnt+2)
dp[SCCs[s]]=1; SCCn[SCCs[s]]-=1
for u in range(SCCs[s],SCCs[e]-1,-1):
    if dp[u]==0: continue
    dp[u]+=SCCn[u]
    for v in aadj[u]:
        dp[v]=max(dp[v],dp[u])
#print(SCCs,SCCn)
#print(aadj)
#print(dp)
print(dp[SCCs[e]])